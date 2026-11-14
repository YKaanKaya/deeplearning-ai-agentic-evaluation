"""Check the selected Git publication files without printing secret values."""

from pathlib import Path
import hashlib
import json
import re
import subprocess
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
result = subprocess.run(
    ["git", "-c", f"safe.directory={ROOT.as_posix()}", "ls-files", "-z"],
    cwd=ROOT, check=True, capture_output=True,
)
files = [ROOT / p for p in result.stdout.decode().split("\0") if p]
tracked = {p.resolve() for p in files}
problems: list[str] = []
local_only_paths = {
    "AGENTS.md", "CHANGELOG.md", "COURSE_PROGRESS.csv", "course-outline.json",
    "labs-index.json", "docs/CAPTURE_WORKFLOW.md", "docs/PORTFOLIO_EVIDENCE.md",
    "docs/PUBLICATION.md",
}
published_notes = {
    "Module-01-foundations-of-evals/notes/01-a-conversation-between-laurie-voss-and-andrew-ng.md",
}
credential_patterns = [
    re.compile(r"(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{30,})"),
    re.compile(r"sk-(?:proj-|ant-)?[A-Za-z0-9_-]{20,}"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"https?://[^\s<>\"]+[?&](?:token|access_token|X-Amz-Signature|sig)=[^\s<>\"]+", re.I),
]
links_checked = 0
for path in files:
    relative = path.relative_to(ROOT).as_posix()
    if relative in local_only_paths or relative.startswith("templates/"):
        problems.append(f"Local capture scaffolding in public Git: {relative}")
    if "/notes/" in relative and relative not in published_notes:
        problems.append(f"Study note has not been selected for publication: {relative}")
    if path.name.startswith(".env") or path.suffix.lower() in {".pdf", ".zip"}:
        problems.append(f"Restricted file: {relative}")
    if relative.startswith("Module-") and path.suffix.lower() != ".md":
        problems.append(f"Unreviewed raw course file: {relative}")
    if path.suffix.lower() in {".gif", ".webp"}:
        continue  # Included frames are reviewed visually; see MEDIA.json.
    text = path.read_text(encoding="utf-8-sig")
    for number, line in enumerate(text.splitlines(), 1):
        if any(pattern.search(line) for pattern in credential_patterns):
            problems.append(f"Potential secret or authenticated URL: {relative}:{number}")
    if path.suffix == ".md":
        if re.search(r"Pending review\. Use `templates/|Status: not yet captured or verified", text):
            problems.append(f"Empty capture template in public Git: {relative}")
        for link in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", text):
            target = link.strip("<>").split("#", 1)[0]
            if not target or re.match(r"^[a-z]+:", target, re.I):
                continue
            links_checked += 1
            resolved = (path.parent / unquote(target)).resolve()
            if resolved not in tracked:
                problems.append(f"Link target absent from public Git: {relative} -> {target}")
    if path.suffix == ".ipynb":
        notebook = json.loads(text)
        errors = [o for c in notebook["cells"] for o in c.get("outputs", [])
                  if o.get("output_type") == "error"]
        if errors:
            problems.append(f"Error in published example: {relative}")

manifest = json.loads((ROOT / "docs/ARTIFACTS.json").read_text(encoding="utf-8"))
for artifact in manifest["artifacts"]:
    path = ROOT / artifact["path"]
    if path.exists() and hashlib.sha256(path.read_bytes()).hexdigest() != artifact["sha256"]:
        problems.append(f"Source artifact changed since audit: {artifact['path']}")

if problems:
    print("\n".join(problems))
    sys.exit(1)
print(f"PASS: {len(files)} publication files, {links_checked} relative links; no detected secrets, "
      "restricted raw files, example errors or changed source hashes")
