from __future__ import annotations

from collections.abc import Iterable

from book_pipeline import EPUB_OUTPUT_DIR, run_output_cli, run_render_epub


def main(argv: Iterable[str] | None = None) -> int:
    return run_output_cli(
        argv,
        description="Convert a markdown chapter into EPUB with pinyin and English translation.",
        default_output_dir=EPUB_OUTPUT_DIR,
        default_suffix="epub",
        runner=run_render_epub,
    )


if __name__ == "__main__":
    raise SystemExit(main())
