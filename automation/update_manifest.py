#!/usr/bin/env python3
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[1]
files=[]
for p in sorted(ROOT.rglob('*')):
 if p.is_file() and '.git' not in p.parts and p.name not in ('MANIFEST.json','SHA256SUMS.txt'):
  files.append({'path':p.relative_to(ROOT).as_posix(),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
(ROOT/'MANIFEST.json').write_text(json.dumps({'name':'universal-build-workflow-v1.0.0','files':files},indent=2)+'\n')
(ROOT/'SHA256SUMS.txt').write_text(''.join(f"{x['sha256']}  {x['path']}\n" for x in files))
