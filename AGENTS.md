# AGENTS

## Active Constraints

- Keep this project fully local and script-driven.
- Do not use LLMs or hosted AI APIs for translation or annotation.
- Use reliable Python libraries only.
- Keep translation models, caches, and outputs inside this repo.
- Make generated reading outputs printable and usable offline.
- Keep format generation separate: HTML, EPUB, and PDF each have their own CLI.
- Do not clear output folders during generation; overwrite matching files only.

## Implementation Notes

- `render_html.py`, `render_epub.py`, and `render_pdf.py` are the output-specific CLI entry points.
- Shared parsing, pinyin, translation, chunking, and packaging logic lives in `book_pipeline.py`.
- Pinyin is generated with `pypinyin`.
- Sentence translation uses `argostranslate` with a local Chinese→English package.
- Translation cache lives in `.cache/sentence_translations.json`.
- Argos data is redirected into `.cache/argos/` so the repo remains self-contained.
- Outputs are organized into `output/html/`, `output/epub/`, and `output/pdf/`.
- PDF rendering uses local WeasyPrint. PDF pinyin layout is converted in-memory for WeasyPrint only; HTML keeps real `<ruby>` markup.
- PDF footers use the output filename label plus page number, e.g. `Chapter 1_1 page 1`, for paper reading.

## Commands

- Install Python deps: `venv/bin/pip install markdown pypinyin argostranslate weasyprint pypdf reportlab`
- Install the offline translation model: `venv/bin/python setup_translate.py`
- Render a chapter HTML: `venv/bin/python render_html.py chapters/Chapter_1.md`
- Render a chapter EPUB: `venv/bin/python render_epub.py chapters/Chapter_1.md`
- Render a chapter PDF: `venv/bin/python render_pdf.py chapters/Chapter_1.md`
- Render all PDFs: `for chapter in chapters/Chapter_{1..10}.md; do venv/bin/python render_pdf.py "$chapter"; done`
- Clear all generated outputs: `rm -rf output/*`
