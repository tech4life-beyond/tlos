#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
MD_FILES = sorted(ROOT.rglob('*.md'))
REQ = {"document_id", "classification", "status", "version", "effective_date", "last_reviewed", "owner"}

NORMATIVE_PATHS = {
    "CONTRIBUTING.md",
    "LICENSE.md",
    "RELEASING.md",
    "docs/index.md",
    "docs/foundation/Tech4Life_Foundation.md",
    "docs/governance/TLOS_Governance_Model.md",
    "docs/product-pipeline/Product_Creation_Pipeline.md",
    "docs/product-factory/Tech4Life_Product_Factory.md",
    "docs/toil-integration/TOIL_Integration_Framework.md",
    "docs/github-architecture/GitHub_Architecture.md",
    "docs/contributor-levels/Contributor_Level_System.md",
    "docs/glossary.md",
    "docs/adr/ADR-001-versioning-convention.md",
    "docs/adr/ADR-002-normative-front-matter-standard.md",
}

errors = []

def slug(s: str) -> str:
    s = s.strip().lower()
    s = re.sub(r"[`*_]", "", s)
    s = re.sub(r"[^a-z0-9\s-]", "", s)
    s = re.sub(r"\s+", "-", s)
    s = re.sub(r"-+", "-", s)
    return s

anchors = {}

for p in MD_FILES:
    rel = p.relative_to(ROOT).as_posix()
    data = p.read_bytes()
    try:
        text = data.decode('utf-8')
    except UnicodeDecodeError as e:
        errors.append(f"{rel}: not valid UTF-8 ({e})")
        continue

    # crude but useful mojibake detector for common UTF-8->Latin1 artifacts
    if re.search(r"[Ãâ�]", text):
        errors.append(f"{rel}: possible mojibake sequence detected")

    file_anchors = set()
    for line in text.splitlines():
        m = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if m:
            file_anchors.add(slug(m.group(2)))
    anchors[rel] = file_anchors

    if rel in NORMATIVE_PATHS:
        fm = re.match(r"\A---\n(.*?)\n---\n", text, flags=re.S)
        if not fm:
            errors.append(f"{rel}: missing YAML front matter")
            continue
        keys = set()
        for ln in fm.group(1).splitlines():
            if ':' in ln:
                keys.add(ln.split(':', 1)[0].strip())
        missing = sorted(REQ - keys)
        if missing:
            errors.append(f"{rel}: missing required metadata keys: {', '.join(missing)}")

link_re = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
for p in MD_FILES:
    rel = p.relative_to(ROOT).as_posix()
    text = p.read_text(encoding='utf-8')
    for target in link_re.findall(text):
        if target.startswith(('http://', 'https://', 'mailto:')):
            continue
        tgt = target.strip()
        if tgt.startswith('#'):
            a = tgt[1:]
            if a and a not in anchors.get(rel, set()):
                errors.append(f"{rel}: broken local anchor #{a}")
            continue
        path, frag = (tgt.split('#', 1) + [''])[:2]
        resolved = (p.parent / path).resolve()
        if not resolved.exists():
            errors.append(f"{rel}: broken relative link {target}")
            continue
        rel_target = resolved.relative_to(ROOT).as_posix()
        if frag and frag not in anchors.get(rel_target, set()):
            errors.append(f"{rel}: broken anchor {target}")

if errors:
    print("Document validation failed:")
    for e in errors:
        print(f"- {e}")
    sys.exit(1)

print("Document validation passed.")
