# Xiaoke · Codex Desktop Pet

**A Codex desktop pet based on a community-created personification of ChatGPT.**

Xiaoke keeps you company while coding, debugging, and waiting for inspiration. A compact chibi anime design with gentle gliding, quiet thinking poses, and consistent proportions between standing and movement.

[中文](README.md) · **English**

![Xiaoke character and motion overview](previews/hero.png)

[Download the asset pack](https://github.com/Ttrrace/xiaoke-pet/raw/refs/heads/main/downloads/xiaoke-pet-v2.zip) · [Transparent sprite sheet](assets/spritesheet-extended.png) · [All animations GIF](previews/all-states.gif) · [MP4 preview](previews/all-states.mp4)

## Animation previews

| Idle → glide right → idle | Idle → gentle float → idle |
| :---: | :---: |
| ![Gentle gliding with consistent character proportions](previews/idle-glide-right-idle.gif) | ![A small upward float followed by a return to the original baseline](previews/idle-jump-idle.gif) |

| Greeting | Waiting for you | Thinking |
| :---: | :---: | :---: |
| ![A small hand wave](previews/states/waving.gif) | ![Hands held together while waiting](previews/states/waiting.gif) | ![A quiet chin-touch thinking pose](previews/states/running.gif) |

| A little disappointed | Reviewing results | Following your gaze |
| :---: | :---: | :---: |
| ![A subdued disappointment and recovery](previews/states/failed.gif) | ![A slight downward gaze while checking results](previews/states/review.gif) | ![Sixteen gaze directions](previews/look-loop.gif) |

## What's included

- One transparent RGBA PNG sprite sheet: **1536 × 2288**, with **192 × 208** cells.
- **Nine animation states and sixteen gaze directions: 73 occupied frames**. Unused cells remain transparent.
- Individual GIFs, state-transition GIFs, a complete MP4 preview, a contact sheet, and a direction sheet.
- Chinese and English documentation, a layout specification, and standalone preview and verification tools.

These flat animated assets are intended for Codex desktop pets and follow the Pets v2 sprite-sheet layout. They are not a Live2D or 3D model. The design is based on a ChatGPT community persona, not an official OpenAI character.

## Usage

### In Codex

1. Download [spritesheet-extended.png](assets/spritesheet-extended.png), preserving its dimensions and transparent background.
2. In Codex with the Pets plugin enabled and custom pets supported, provide the PNG to your assistant. For example:

   > Validate this v2 pet sprite sheet, create a custom pet named Xiaoke, and select it.

3. Let the Pets tools validate, upload, create, and select the pet. If you already have a pet with that name, specify which existing pet you want to update.

Your client must support these features; this repository does not install or enable the plugin. **Frame timing, mouse triggers, and loop counts are controlled by the client.** Replacing the sprite sheet does not change those settings. The GIFs show the export timing; actual playback also depends on client scaling and animation scheduling.

### In another project

Crop frames using the [layout specification](docs/format.md). The state named `running` means focused work or thinking; `running-left` and `running-right` are directional movement. The movement artwork depicts a gentle glide.

```bash
python -m pip install -r requirements.txt
python tools/verify_assets.py
python tools/preview.py --output-dir build/previews
```

The tools require only Pillow. The preview script crops existing pixels without redrawing the character. Generated files go into the Git-ignored `build/` directory.

## Repository layout

```text
assets/                     Transparent sheet and frame-layout metadata
previews/                   Cover, GIFs, MP4, and comparison sheets
previews/states/            Nine individual animation states
downloads/                 Ready-to-download asset pack
docs/format.md             Bilingual sprite-sheet specification
tools/                     Preview and file-integrity tools
LICENSES/                  Full license texts
```

[Frame contact sheet](previews/contact-sheet.png) · [Sixteen-direction sheet](previews/direction-sheet.png)

## Version and validation

This is the **second artwork revision**, published as `2.0.0`. It focuses on consistent proportions, movement poses, hand anatomy, and restrained loops.

- Passed v2 structural validation and the Pets service's file validation.
- Reviewed frame by frame, with three independent blind direction reviews.
- Downloaded again after upload; decoded RGBA pixels matched this repository's sprite sheet.
- Gaze differences near vertical directions are intentionally subtle. Some drawing variation remains across states; this is not a rigged model.

These checks apply to the current files and do not imply that interaction has been tested in every client. Run `tools/verify_assets.py` to compare local files with [manifest.json](manifest.json).

## Reuse and attribution

**Artwork and documentation: CC BY 4.0. Tool code: MIT.** Share, modify, and reuse them under the applicable license. Suggested attribution:

> Xiaoke / 小柯 by Ttrrace — https://github.com/Ttrrace/xiaoke-pet — CC BY 4.0. Indicate any changes you make.

See [CREDITS.md](CREDITS.md) and [LICENSE.md](LICENSE.md) for character references, generation details, and license scope. Please report motion transitions, transparency issues, or proportion problems in [Issues](https://github.com/Ttrrace/xiaoke-pet/issues), ideally with the state name and frame index.
