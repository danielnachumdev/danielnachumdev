# Profile README generator – Agent Context

Implementation guide for coding agents changing this **generator**. User-facing tool docs: [`TOOL.md`](TOOL.md).

**Do not treat [`README.md`](README.md) as the tool’s marketing page.** This is the special GitHub profile repository (`danielnachumdev/danielnachumdev`); `README.md` is the **generated product** rendered on the profile. Document the tool in `TOOL.md` / this file.

---

## Orientation

| Question | Answer |
| -------- | ------ |
| What is this? | Python script + small object model that **writes** the GitHub profile `README.md` |
| Entry point | `generate_md.py` → overwrites `./README.md` |
| Library code | `src/` (`objects.py`, `tags.py`; re-exported via `src/__init__.py`) |
| Toolchain | Plain Python + optional `requirements.txt` (`pylint`, `mypy`) — **no** `pyproject.toml` / uv yet |
| Runtime deps | **stdlib only** (`datetime`, `urllib.parse`, `json`, `abc`, `typing`) |
| Tests | None today |
| Secrets | None required; never commit tokens, `.env`, or API keys |

```text
.
├── generate_md.py   # Profile content config + writer
├── src/
│   ├── __init__.py  # Re-exports tags + objects
│   ├── objects.py   # Markdownable, Text, Tag
│   └── tags.py      # Section, headings, Image, IconSvg, lists, TypingText, …
├── README.md        # GENERATED profile README (product output)
├── TOOL.md          # Marketing / user docs for the generator
├── requirements.txt # Dev-only: pylint, mypy
├── LICENSE          # MIT
└── AGENTS.md
```

Shared CI/CD (when present on `main`): [`danielnachumdev/actions`](https://github.com/danielnachumdev/actions). How to adopt: [`HOW-TO-USE.md`](https://github.com/danielnachumdev/actions/blob/v1/HOW-TO-USE.md).

---

## Develop

```bash
python generate_md.py
# optional
pip install -r requirements.txt
pylint generate_md.py src
mypy generate_md.py src
```

| Task | Command |
| ---- | ------- |
| Regenerate profile README | `python generate_md.py` |
| Lint (if installed) | `pylint generate_md.py src` |
| Types (if installed) | `mypy generate_md.py src` |

### Changing profile content

1. Edit `USERNAME`, `LANGUAGES_AND_TOOLS`, `REPOS_TO_HIGHLIGHT`, `STATISTICS_SRC`, and/or the `README` list in `generate_md.py`.
2. Run `python generate_md.py`.
3. Commit **both** script changes and the regenerated `README.md` when the profile should update.
4. Prefer new building blocks as classes in `src/tags.py` (or `objects.py`) rather than string-concat in `generate_md.py`.

### Domain notes

- Public helpers are listed in `src/tags.py` `__all__` and pulled into `generate_md.py` via `from src import *`.
- `IconSvg` loads Devicon SVGs: `…/icons/{name}/{name}-original.svg` — names must match that catalog.
- `TypingText` builds a [readme-typing-svg](https://github.com/DenverCoder1/readme-typing-svg) URL; `Repository` links to `https://www.github.com/{user}/{name}`.
- External badge hosts (github-readme-stats, streak-stats, typing-svg) are third-party; keep URLs configurable in `generate_md.py`.
- Follow the writing-python skill when adding modules (class-first, SRP files, no stub shims).

---

## PRs, CI, and releases

1. Branch off `main`; open a PR into `main`.
2. Attach **exactly one** semver label: `noBump` | `bumpPatch` | `bumpMinor` | `bumpMajor`.
3. Prefer **`CI / CI`** and **`Semver / Semver`** when those checks exist (thin orchestrators from `danielnachumdev/actions`).
4. This repo is **not** a PyPI package; there is no publish/CD wheel path. Prefer **`noBump`** for docs and generator fixes unless a real versioning scheme is introduced.
5. Dependabot PRs stay on `noBump`.
6. Change shared CI/semver behavior in **`danielnachumdev/actions`**, not by re-vendoring here.

---

## Sensitive / ignored

Do not commit: `.env`, API keys, tokens, or unrelated secrets. Respect `.gitignore`. Regenerating `README.md` only updates public profile markup — still avoid pasting private URLs or credentials into `generate_md.py`.
