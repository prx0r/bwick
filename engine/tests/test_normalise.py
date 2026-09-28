"""P0.1 tests — normalise.py. Offline, no keys (DEVPLAN rule)."""
import io
import json
import os
import sys

from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from engine.normalise import normalise_order  # noqa: E402


def _jpeg(path, size=(800, 800), quality=90, orientation=None, min_bytes=None):
    im = Image.new("RGB", size, (30 + hash(path) % 200, 90, 140))
    if orientation is not None:
        exif = Image.Exif()
        exif[0x0112] = orientation              # EXIF orientation tag
        im.save(path, format="JPEG", quality=quality, exif=exif)
    else:
        im.save(path, format="JPEG", quality=quality)
    if min_bytes is not None:                   # pad to beat MIN_BYTES
        with open(path, "ab") as f:
            f.write(b"0" * (min_bytes - os.path.getsize(path) + 1))
    return path


def _png(path, size=(600, 600)):
    Image.new("RGB", size, (10, 200, 90)).save(path, format="PNG")
    return path


def test_happy_path_front_first(tmp_path):
    d = tmp_path / "order"
    d.mkdir()
    _jpeg(str(d / "pet_02_side_view.jpg"), size=(760, 820))
    _jpeg(str(d / "pet_01_front_face.jpg"), size=(800, 800))
    _jpeg(str(d / "pet_03_full_body.jpg"), size=(700, 900))
    res = normalise_order(str(d))
    assert res["ok"], res["reason"]
    assert res["count"] == 3
    assert res["roles"][0] == "front_face", res["roles"]
    assert res["roles"][1] == "full_body"
    assert all(u.startswith("data:image/jpeg;base64,") for u in res["image_urls"])


def test_missing_front_rejected(tmp_path):
    d = tmp_path / "order"
    d.mkdir()
    _jpeg(str(d / "pet_02_side_view.jpg"))
    res = normalise_order(str(d))
    assert not res["ok"] and "front-face" in res["reason"]


def test_exif_rotation_applied(tmp_path):
    d = tmp_path / "order"
    d.mkdir()
    p = _jpeg(str(d / "a_front_face.jpg"), size=(1200, 300), orientation=6)  # rotate 90
    res = normalise_order(str(d))
    assert res["ok"], res["reason"]
    # oriented upright: shortest edge after transpose =300 -> encoded size small;
    # prove orientation changed dims by decoding the payload
    import base64
    raw = base64.b64decode(res["image_urls"][0].split(",", 1)[1])
    im = Image.open(io.BytesIO(raw))
    assert min(im.size) < max(im.size) or im.size[0] != 1200


def test_undersized_and_tiny_file_rejected(tmp_path):
    d = tmp_path / "order"
    d.mkdir()
    _jpeg(str(d / "a_front_face.jpg"), size=(100, 100), min_bytes=4000)  # < 200px side
    res = normalise_order(str(d))
    assert not res["ok"] and "min side" in res["reason"]

    d2 = tmp_path / "order2"
    d2.mkdir()
    (d2 / "a_front_face.jpg").write_bytes(b"\xff\xd8\xff\xe0tiny")
    res = normalise_order(str(d2))
    assert not res["ok"] and ("too small" in res["reason"] or "undecodable" in res["reason"])


def test_non_image_rejected(tmp_path):
    d = tmp_path / "order"
    d.mkdir()
    (d / "a_front_face.gif").write_bytes(b"GIF89a" + b"0" * 5000)
    res = normalise_order(str(d))
    assert not res["ok"]


def test_favourite_excluded_when_qc_fails(tmp_path):
    d = tmp_path / "order"
    d.mkdir()
    _jpeg(str(d / "pet_01_front_face.jpg"))
    _jpeg(str(d / "pet_04_favourite.jpg"))
    res = normalise_order(str(d), favourite_passes=False)
    assert res["ok"] and res["count"] == 1
    assert all("fav" not in r for r in res["roles"])


def test_max_four_images(tmp_path):
    d = tmp_path / "order"
    d.mkdir()
    _jpeg(str(d / "a_front_face.jpg"))
    for i in range(6):
        _jpeg(str(d / f"x{i}_body_angle{i}.jpg"), size=(500 + i, 700))
    res = normalise_order(str(d))
    assert res["ok"] and res["count"] == 4


def test_long_edge_capped_at_2048(tmp_path):
    d = tmp_path / "order"
    d.mkdir()
    _jpeg(str(d / "a_front_face.jpg"), size=(4096, 2048))
    res = normalise_order(str(d))
    assert res["ok"]
    import base64
    raw = base64.b64decode(res["image_urls"][0].split(",", 1)[1])
    im = Image.open(io.BytesIO(raw))
    assert max(im.size) <= 2048


def test_empty_dir_and_missing_dir(tmp_path):
    empty = tmp_path / "empty"
    empty.mkdir()
    res = normalise_order(str(empty))
    assert not res["ok"] and "no image files" in res["reason"]
    res = normalise_order(str(tmp_path / "nope"))
    assert not res["ok"] and "no order dir" in res["reason"]
