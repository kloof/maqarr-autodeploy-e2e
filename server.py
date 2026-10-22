"""Disposable real-VM lifecycle fixture. Never run as a host diagnostic."""
import http.server
import json
import os
import threading
import time
import uuid

INSTANCE = uuid.uuid4().hex


class Handler(http.server.BaseHTTPRequestHandler):
    def reply(self, status, value):
        body = json.dumps(value).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/slow":
            time.sleep(20)
        self.reply(200, {"ok": True, "version": "maqarr-auto-e2e:python:ci-fail", "instance": INSTANCE})

    def do_POST(self):
        if self.path == "/exit":
            print("Known lifecycle fixture: requested app exit", flush=True)
            self.reply(202, {"exiting": True, "instance": INSTANCE})
            threading.Timer(0.5, lambda: os._exit(17)).start()
        else:
            self.reply(404, {"error": "unknown_path"})

    def log_message(self, _format, *args):
        pass


if __name__ == "__main__":
    print("maqarr-auto-e2e:python:ci-fail ready", flush=True)
    http.server.HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()
