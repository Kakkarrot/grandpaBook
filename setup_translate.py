from __future__ import annotations

from collections.abc import Iterable

from book_pipeline import run_setup_cli


def main(argv: Iterable[str] | None = None) -> int:
    return run_setup_cli(argv)


if __name__ == "__main__":
    raise SystemExit(main())
