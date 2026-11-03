# Profile README generator

**Small Python tool that builds this repo’s GitHub profile `README.md`** from typed markdown/HTML objects — stats badges, typing SVG, language icons, and highlighted repos — instead of hand-editing markup.

> **Note:** [`README.md`](./README.md) is the **generated profile page** (GitHub special-username repo). This file documents the **generator**. Agent/dev workflow: [`AGENTS.md`](./AGENTS.md).

Requires **Python 3** (stdlib only at runtime).

## Why this exists

A personal profile README is mostly HTML-ish markdown: icons, badges, and lists that are tedious to keep consistent. This tool composes sections as objects (`Section`, `Heading`, `IconSvg`, `TypingText`, …), then writes `README.md` in one shot.

- **Object model** — `Markdownable` types in `src/` render to markdown/HTML
- **One entry script** — edit lists/sections in `generate_md.py`, run it, commit the output
- **Profile-shaped output** — typing SVG, GitHub stats/streak widgets, Devicon icons, highlighted repo links
- **MIT licensed** — see [`LICENSE`](./LICENSE)

## Quick start

```bash
git clone https://github.com/danielnachumdev/danielnachumdev.git
cd danielnachumdev
python generate_md.py   # overwrites ./README.md
```

No runtime `pip install` is required. Optional lint/type tools:

```bash
pip install -r requirements.txt   # pylint, mypy
```

## Customize

Edit constants and the `README` object list in [`generate_md.py`](./generate_md.py):

| Knob | Role |
| ---- | ---- |
| `USERNAME` | GitHub user for stats URLs and repo links |
| `LANGUAGES_AND_TOOLS` | Devicon names → `IconSvg` row |
| `REPOS_TO_HIGHLIGHT` | Repo names under that user |
| `STATISTICS_SRC` | Extra badge image URLs (top langs, streak, …) |
| `README` | Ordered sections (`Heading*`, `TypingText`, `Section`, …) |

Then regenerate and commit both the script (if changed) and `README.md`.

## What you get

| Piece | Role |
| ----- | ---- |
| `generate_md.py` | Profile content + `main()` writer |
| `src/objects.py` | `Markdownable`, `Text`, `Tag` |
| `src/tags.py` | `Section`, headings, `Image`, `IconSvg`, lists, `Repository`, `TypingText`, … |
| `README.md` | **Product output** shown on the GitHub profile |

## Contributing & development

See [`AGENTS.md`](./AGENTS.md).

## License

MIT — see [`LICENSE`](./LICENSE).
