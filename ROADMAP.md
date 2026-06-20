# Roadmap

## Current Scope

Convert Chinese Markdown chapters into local, offline reading outputs:

- printable HTML
- EPUB
- paginated PDF

Every output should preserve the study-reader format:

- pinyin above each Chinese character
- English translation below each Chinese sentence
- sentence-safe chunking around 5,000 text units by default

## Features

- `render_html.py` renders chapter Markdown into `output/html/`.
- `render_epub.py` renders chapter Markdown into `output/epub/`.
- `render_pdf.py` renders chapter Markdown into `output/pdf/`.
- `setup_translate.py` installs the offline Chinese-to-English Argos model.
- `book_pipeline.py` owns shared parsing, pinyin annotation, translation, chunking, templates, and output helpers.
- PDF rendering uses WeasyPrint and stamps filename-based footers such as `Chapter 1_1 page 1`.
- Long renders print progress logs while loading, preparing chunks, rendering, writing, and saving the translation cache.

## Decisions

- Keep the project fully local and script-driven.
- Do not use LLMs or hosted AI APIs for translation or annotation.
- Use `pypinyin` for pinyin annotation.
- Use `argostranslate` with a local Chinese-to-English package for sentence translation.
- Cache sentence translations in `.cache/sentence_translations.json`.
- Keep Argos data under `.cache/argos/` so model data stays inside the repo.
- Keep format generation separate: one CLI per output format.
- Keep shared rendering behavior DRY in `book_pipeline.py`.
- Do not clear output folders automatically; generation overwrites matching files and preserves unrelated outputs.
- Preserve real `<ruby>` markup in HTML. Convert ruby to PDF-compatible stacked spans only inside the PDF rendering path.
