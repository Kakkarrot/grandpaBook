# Roadmap

## Current Goal

Convert Chinese markdown chapters into printable HTML where:

- every Chinese character has pinyin above it
- every Chinese sentence has an English translation below it
- the output is readable on paper without network access

## Decisions Locked In

- Use Python libraries, not LLMs.
- Keep all generated assets local to the repo.
- Use local translation instead of a billed cloud API.
- Cache sentence translations so repeated renders are cheap.
- Prefer a simple, dependable CLI over a larger app.

## Work Items

- [x] Initialize this folder as a git repo.
- [x] Install the Python libraries for markdown, pinyin, and translation.
- [x] Build the conversion CLI in `main.py`.
- [x] Keep the project on a local Argos-based translation path.
- [x] Download the Argos Chinese→English model into the repo cache.
- [x] Render `chapters/Chapter_1.md` into printable HTML.
- [x] Split long chapter renders into numbered sentence-safe chunks of about 5,000 text units.
- [x] Organize generated outputs into separate `output/html/` and `output/epub/` folders.
- [x] Review the output for pagination and translation quality.
