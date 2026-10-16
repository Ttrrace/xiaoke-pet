"""Export GIF previews from the published atlas without changing its pixels."""
import argparse
import json
from pathlib import Path

from PIL import Image


def main():
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path, default=root / 'build/previews')
    args = parser.parse_args()
    layout = json.loads((root / 'assets/layout.json').read_text(encoding='utf-8'))
    atlas = Image.open(root / 'assets/spritesheet-extended.png').convert('RGBA')
    assert atlas.size == tuple(layout['size']), 'Unexpected atlas dimensions'
    width, height = layout['cell_size']
    args.output_dir.mkdir(parents=True, exist_ok=True)

    def frame(row, column):
        tile = atlas.crop((column * width, row * height, (column + 1) * width, (row + 1) * height))
        background = Image.new('RGBA', tile.size, '#edf2f4')
        background.alpha_composite(tile)
        return background.convert('RGB')

    def gif(name, frames, durations):
        frames[0].save(args.output_dir / name, save_all=True, append_images=frames[1:], duration=durations, loop=0, disposal=2, optimize=False)

    for state in layout['states']:
        gif(state['key'] + '.gif', [frame(state['row'], col) for col in range(state['frames'])], state['preview_durations_ms'])
    gif('look-loop.gif', [frame(9 + index // 8, index % 8) for index in range(16)], [180] * 16)
    print(f'Exported 9 state GIFs and a look loop to {args.output_dir}')


if __name__ == '__main__':
    main()
