from __future__ import annotations

from collections.abc import Iterable

from book_pipeline import HTML_OUTPUT_DIR, run_output_cli, run_render_html


def main(argv: Iterable[str] | None = None) -> int:
    return run_output_cli(
        argv,
        description="Convert a markdown chapter into HTML with pinyin and English translation.",
        default_output_dir=HTML_OUTPUT_DIR,
        default_suffix="html",
        runner=run_render_html,
    )


if __name__ == "__main__":
    raise SystemExit(main())
