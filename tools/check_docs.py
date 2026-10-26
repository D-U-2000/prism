"""Check required documents and local Markdown file links; no network calls."""
import pathlib
import re
import sys
from urllib.parse import unquote

root = pathlib.Path(__file__).resolve().parents[1]
errors = []
required = ['README.md', 'AGENTS.md', 'docs/README.md',
            'docs/standards/documentation.md', 'docs/standards/method.md']
for name in required:
    path = root / name
    if not path.is_file() or not path.read_text(encoding='utf-8').strip():
        errors.append(f'Missing or empty: {name}')
files = list(root.glob('*.md')) + list((root / 'docs').rglob('*.md'))
for path in files:
    content = path.read_text(encoding='utf-8')
    if not content.startswith('# '):
        errors.append(f'{path.relative_to(root)}: missing title')
    for link in re.findall(r'\]\(([^\s)]+)\)', content):
        if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', link) or link.startswith('#'):
            continue
        target = unquote(link.split('#')[0])
        if target and not (path.parent / target).exists():
            errors.append(f'{path.relative_to(root)}: broken file link {link}')
for error in errors:
    print(error)
print(f'Checked {len(files)} documents; {len(errors)} errors. External URLs, anchors and semantic accuracy are not checked.')
sys.exit(bool(errors))
