#!/usr/bin/env python3
"""Roast.pet Card Studio — browser UI backed by the same MCP engine as Muse."""
import json, os, sys, hashlib, secrets, base64
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse
from pathlib import Path

ROOT = os.path.dirname(os.path.abspath(__file__))
FUNNYLABS = os.path.dirname(ROOT)
sys.path.insert(0, FUNNYLABS)

from humour_mcp.mcp_server import handle as mcp_handle

TOKEN = os.environ.get("DASH_TOKEN", secrets.token_urlsafe(24))

class Handler(BaseHTTPRequestHandler):
    def _gate(self):
        q = parse_qs(urlparse(self.path).query)
        if q.get("token", [""])[0] != TOKEN:
            self.send_response(401); self.end_headers(); self.wfile.write(b"bad token"); return False
        return True

    def _json(self, obj, code=200):
        data = json.dumps(obj).encode()
        self.send_response(code); self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data))); self.end_headers(); self.wfile.write(data)

    def _body(self):
        try: n = int(self.headers.get("Content-Length", 0))
        except: n = 0
        if not n: return {}
        try: return json.loads(self.rfile.read(n))
        except: return {}

    def do_GET(self):
        if not self._gate(): return
        path = urlparse(self.path).path
        if path in ("/", "/index.html"):
            page = open(os.path.join(ROOT, "static", "index.html"), "rb").read()
            self.send_response(200); self.send_header("Content-Type", "text/html")
            self.send_header("Content-Length", str(len(page))); self.end_headers(); self.wfile.write(page)
        elif path == "/api/templates":
            self._json(mcp_handle("funny.list_templates", {}))
        elif path.startswith("/cards/"):
            # Serve rendered card PNGs (see render_cards.py)
            fname = os.path.basename(path.split("/cards/", 1)[1])
            if not fname.endswith(".png") or "/" in fname or fname.startswith("."):
                self.send_response(400); self.end_headers(); return
            fpath = os.path.join(ROOT, "static", "cards", fname)
            if os.path.exists(fpath):
                data = open(fpath, "rb").read()
                self.send_response(200); self.send_header("Content-Type", "image/png")
                self.send_header("Content-Length", str(len(data))); self.send_header("Cache-Control", "public, max-age=3600"); self.end_headers(); self.wfile.write(data)
            else:
                self.send_response(404); self.end_headers()
        elif path.startswith("/photo-card/"):
            # Render one template WITH an avatar/photo circled in.
            # ?photo=<tmp fname> or ?avatar=<avatar id> (&token=) — cached to /tmp.
            from humour_mcp.templates import TEMPLATE_MAP
            tid = os.path.basename(path.split("/photo-card/", 1)[1]).replace(".png", "")
            q = parse_qs(urlparse(self.path).query)
            photo = os.path.basename(q.get("photo", [""])[0])
            avatar_id = os.path.basename(q.get("avatar", [""])[0])
            src = None
            cache_key = ""
            if avatar_id:
                sys.path.insert(0, FUNNYLABS)
                from humour_mcp.avatar import photo_path as avatar_photo
                src = avatar_photo(avatar_id)
                cache_key = "av_" + avatar_id
            elif photo and "/" not in photo and not photo.startswith("."):
                src = os.path.join("/tmp/roast_uploads", photo)
                cache_key = "up_" + photo
            if tid not in TEMPLATE_MAP or not src or not os.path.exists(src):
                self.send_response(404 if tid in TEMPLATE_MAP else 400); self.end_headers(); return
            cache = f"/tmp/roast_card_{tid}_{hashlib.md5(cache_key.encode()).hexdigest()[:10]}.png"
            if not os.path.exists(cache):
                sys.path.insert(0, FUNNYLABS)
                from render_cards import render_with_photo
                render_with_photo(tid, src, cache)
            data = open(cache, "rb").read()
            self.send_response(200); self.send_header("Content-Type", "image/png")
            self.send_header("Content-Length", str(len(data))); self.end_headers(); self.wfile.write(data)
        elif path == "/api/avatars":
            sys.path.insert(0, FUNNYLABS)
            from humour_mcp.avatar import list_avatars
            self._json({"avatars": list_avatars()})
        elif path.startswith("/previews/"):
            # Serve rendered preview files from /tmp
            fpath = "/tmp/" + path.split("/previews/", 1)[1]
            if os.path.exists(fpath):
                data = open(fpath, "rb").read()
                self.send_response(200); self.send_header("Content-Type", "text/html")
                self.send_header("Content-Length", str(len(data))); self.end_headers(); self.wfile.write(data)
            else:
                self.send_response(404); self.end_headers()
        else:
            self.send_response(404); self.end_headers()

    def do_POST(self):
        if not self._gate(): return
        path = urlparse(self.path).path
        if path == "/api/upload":
            # Multipart: read raw bytes ONCE here (must not go through _body(),
            # which would consume rfile before we parse the file out of it).
            try:
                content_len = int(self.headers.get("Content-Length", 0))
            except (TypeError, ValueError):
                content_len = 0
            self._upload_raw(self.rfile.read(content_len) if content_len > 0 else b"")
            return
        body = self._body()
        if path == "/api/create-card":
            self._json(mcp_handle("funny.create_card", body))
        elif path == "/api/avatar":
            # Create persistent avatar from an uploaded tmp photo.
            # Body: {photo: <tmp fname>, name, species}
            sys.path.insert(0, FUNNYLABS)
            from humour_mcp.avatar import create_avatar
            tmp = os.path.basename(str(body.get("photo", "")))
            src = os.path.join("/tmp/roast_uploads", tmp)
            if not tmp or "/" in tmp or not os.path.exists(src):
                self._json({"error": "photo not found; upload first"}, 400)
            else:
                try:
                    rec = create_avatar(src, str(body.get("name", "Pet")),
                                        str(body.get("species", "")))
                    self._json({"avatar": rec})
                except Exception as e:
                    self._json({"error": str(e)[:200]}, 500)
        elif path == "/api/preview":
            self._json(mcp_handle("funny.preview_card", body))
        elif path == "/api/quote":
            self._json(mcp_handle("funny.quote_card", body))
        elif path == "/api/order":
            self._json(mcp_handle("funny.order_card", body))
        else:
            self.send_response(404); self.end_headers()

    def _upload_raw(self, body: bytes):
        """Parse one multipart photo upload from already-read raw bytes."""
        upload_dir = "/tmp/roast_uploads"
        os.makedirs(upload_dir, exist_ok=True)
        content_type = self.headers.get("Content-Type", "")
        import re
        m = re.search(r"boundary=([^;]+)", content_type)
        if m and body:
            bound = ("--" + m.group(1).strip().strip('"')).encode()
            for p in body.split(bound):
                if b'name="photo"' not in p:
                    continue
                hdr_end = p.find(b"\r\n\r\n")
                if hdr_end < 0:
                    continue
                fmatch = re.search(rb'filename="([^"]*)"', p[:hdr_end])
                fname_in = fmatch.group(1).decode("utf-8", "replace") if fmatch else "upload.jpg"
                data = p[hdr_end + 4:]
                if data.endswith(b"\r\n"):
                    data = data[:-2]
                ext = os.path.splitext(fname_in)[1] or ".jpg"
                fname = hashlib.md5(fname_in.encode()).hexdigest()[:12] + ext
                fpath = os.path.join(upload_dir, fname)
                with open(fpath, "wb") as f:
                    f.write(data)
                self._json({"url": f"/uploads/{fname}", "path": fpath})
                return
        self._json({"error": "no file"}, 400)

    def log_message(self, *a): pass

if __name__ == "__main__":
    port = int(os.environ.get("STUDIO_PORT", "8792"))
    print(f"Roast.pet Card Studio: http://localhost:{port}/?token={TOKEN}")
    ThreadingHTTPServer(("0.0.0.0", port), Handler).serve_forever()
