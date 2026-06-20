from __future__ import annotations

from collections.abc import Iterable

from book_pipeline import PDF_OUTPUT_DIR, run_output_cli, run_render_pdf


def main(argv: Iterable[str] | None = None) -> int:
    return run_output_cli(
        argv,
        description="Convert a markdown chapter into paginated PDF with pinyin and English translation.",
        default_output_dir=PDF_OUTPUT_DIR,
        default_suffix="pdf",
        runner=run_render_pdf,
    )


if __name__ == "__main__":
    raise SystemExit(main())
