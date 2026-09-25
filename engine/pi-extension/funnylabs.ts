import { spawn, ChildProcess } from "child_process";
import { readFileSync } from "fs";
import { join } from "path";

interface McpRequest {
  jsonrpc: "2.0";
  id: number;
  method: string;
  params?: any;
}

interface McpResponse {
  jsonrpc: "2.0";
  id: number;
  result?: any;
  error?: any;
}

let proc: ChildProcess | null = null;
let msgId = 0;
const pending = new Map<number, { resolve: (v: any) => void; reject: (e: Error) => void }>();
let buffer = "";

function spawnServer(): ChildProcess {
  const serverPath = join(__dirname, "..", "humour_mcp", "mcp_server.py");
  const p = spawn("python3", [serverPath, "--serve"], {
    stdio: ["pipe", "pipe", "pipe"],
  });
  p.stdout!.on("data", (data: Buffer) => {
    buffer += data.toString();
    const lines = buffer.split("\n");
    buffer = lines.pop()!;
    for (const line of lines) {
      if (!line.trim()) continue;
      try {
        const msg: McpResponse = JSON.parse(line);
        const handler = pending.get(msg.id);
        if (handler) {
          pending.delete(msg.id);
          if (msg.error) handler.reject(new Error(JSON.stringify(msg.error)));
          else handler.resolve(msg.result);
        }
      } catch {}
    }
  });
  p.stderr!.on("data", (data: Buffer) => {
    console.error("mcp stderr:", data.toString());
  });
  p.on("exit", () => {
    proc = null;
    for (const [, h] of pending) h.reject(new Error("server exited"));
    pending.clear();
  });
  return p;
}

function call(method: string, params: any = {}): Promise<any> {
  if (!proc) proc = spawnServer();
  const id = ++msgId;
  const req: McpRequest = { jsonrpc: "2.0", id, method, params };
  return new Promise((resolve, reject) => {
    pending.set(id, { resolve, reject });
    proc!.stdin!.write(JSON.stringify(req) + "\n");
    setTimeout(() => {
      if (pending.has(id)) {
        pending.delete(id);
        reject(new Error("timeout"));
      }
    }, 59000);
  });
}

export async function shutdown() {
  if (proc) proc.kill();
}

// pi-exposed tools

export async function funny_list(opts: { occasion?: string; product?: string; topical?: boolean } = {}) {
  const r = await call("tools/call", { name: "funny.list_templates", arguments: opts });
  return JSON.stringify(r, null, 2);
}

export async function funny_concepts(opts: {
  recipient_name: string; occasion: string; facts: string[];
  roast_level?: string; pet_name?: string; pet_species?: string;
  template_id?: string; topical_context?: string;
}) {
  const r = await call("tools/call", { name: "funny.create_concepts", arguments: opts });
  return JSON.stringify(r, null, 2);
}

export async function funny_preview(opts: {
  candidate_id: string; template_id: string; setup: string;
  punchline: string; visual: string; roast_level?: string;
  recipient_name: string; pet_image_url?: string;
}) {
  const r = await call("tools/call", { name: "funny.preview_card", arguments: opts });
  return JSON.stringify(r, null, 2);
}

export async function funny_card(opts: {
  recipient_name: string; occasion: string; facts: string[];
  roast_level?: string; pet_name?: string; pet_species?: string;
  pet_image_url?: string; template_id?: string; topical_context?: string;
}) {
  const r = await call("tools/call", { name: "funny.create_card", arguments: opts });
  return JSON.stringify(r, null, 2);
}

export async function funny_quote(opts: { destination: string; card_spec: any }) {
  const r = await call("tools/call", { name: "funny.quote_card", arguments: opts });
  return JSON.stringify(r, null, 2);
}

export async function funny_order(opts: { render_path: string; shipping_address: any; shipping_method?: string }) {
  const r = await call("tools/call", { name: "funny.order_card", arguments: opts });
  return JSON.stringify(r, null, 2);
}

export async function funny_verify() {
  const r = await call("tools/call", { name: "funny.verify_chain", arguments: {} });
  return JSON.stringify(r, null, 2);
}
