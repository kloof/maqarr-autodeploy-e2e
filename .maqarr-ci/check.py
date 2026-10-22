from pathlib import Path
import hashlib, json
root = Path(__file__).resolve().parents[1]
meta = json.loads((root / ".maqarr-ci/fixture.json").read_text())
for name, expected in meta["source_sha256"].items():
    source = root / name
    assert source.is_file() and not source.is_symlink(), "Missing known source"
    assert hashlib.sha256(source.read_bytes()).hexdigest() == expected, "Source changed"
text = (root / meta["entry"]).read_text()
assert meta["marker"] in text, "Response marker missing"
assert meta["log_marker"] in text, "Startup marker missing"
assert meta["ci_pass"], "Deliberate CI failure fixture"
print("Known fixture structure passed: " + meta["marker"])
