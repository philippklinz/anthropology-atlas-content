#!/usr/bin/env python3
"""Optional file integrity check, not historical or semantic validation."""
from pathlib import Path
import hashlib
import json
root=Path(__file__).resolve().parents[1]/'published'
catalog=json.loads((root/'catalog.json').read_text())
for entry in catalog['files']:
    path=(root/entry['path']).resolve()
    assert path.is_relative_to(root.resolve()), entry['path']
    data=path.read_bytes()
    assert len(data)==entry['bytes'], entry['path']
    assert hashlib.sha256(data).hexdigest()==entry['sha256'], entry['path']
print('Published file hashes verified. Semantic validation: open tooling/index.html.')
