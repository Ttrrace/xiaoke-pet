"""Check published file hashes and sprite occupancy; no quality/moderation claim."""
import hashlib
import json
from pathlib import Path

from PIL import Image


def main():
    root = Path(__file__).resolve().parents[1]
    manifest = json.loads((root / 'manifest.json').read_text(encoding='utf-8'))
    errors = []
    for name, expected in manifest['files'].items():
        path = root / name
        if not path.is_file():
            errors.append(f'Missing file: {name}')
            continue
        data = path.read_bytes()
        if len(data) != expected['bytes'] or hashlib.sha256(data).hexdigest() != expected['sha256']:
            errors.append(f'File differs from manifest: {name}')
    layout = json.loads((root / 'assets/layout.json').read_text(encoding='utf-8'))
    with Image.open(root / 'assets/spritesheet-extended.png') as atlas:
        if atlas.size != tuple(layout['size']) or atlas.mode != 'RGBA':
            errors.append('Atlas must be the original 1536x2288 RGBA PNG')
        else:
            width, height = layout['cell_size']
            alpha = atlas.getchannel('A')
            for row, count in enumerate(layout['frames_per_row']):
                for column in range(8):
                    occupied = alpha.crop((column * width, row * height, (column + 1) * width, (row + 1) * height)).getbbox() is not None
                    if occupied != (column < count):
                        errors.append(f'Unexpected occupancy: row {row}, column {column}')
    if errors:
        raise SystemExit('\n'.join(errors))
    print(f'PASS: {len(manifest["files"])} file hashes; 73 occupied and 15 transparent cells.')


if __name__ == '__main__':
    main()
