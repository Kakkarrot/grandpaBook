# AGENTS

## Active Constraints

- Keep this project fully local and script-driven.
- Do not use LLMs or hosted AI APIs for translation or annotation.
- Use reliable Python libraries only.
- Keep translation models, caches, and outputs inside this repo.
- Make the final HTML printable for offline reading.

## Implementation Notes

- `main.py` is the CLI entry point.
- Pinyin is generated with `pypinyin`.
- Sentence translation uses `argostranslate` with a local Chinese→English package.
- Translation cache lives in `.cache/sentence_translations.json`.
- Argos data is redirected into `.cache/argos/` so the repo remains self-contained.

## Commands

- Install Python deps: `venv/bin/pip install markdown pypinyin argostranslate`
- Install the offline translation model: `venv/bin/python main.py setup-translate`
- Render a chapter: `venv/bin/python main.py render chapters/Chapter_1.md`
