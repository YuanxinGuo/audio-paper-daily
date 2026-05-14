"""End-to-end runner: fetch -> analyze -> render -> rankings."""
import fetch_arxiv
import fetch_hf
import analyze
import render
import rankings


def main() -> None:
    # Each fetcher is best-effort. The pipeline must continue even if one
    # source is rate-limited or temporarily down.
    try:
        fetch_arxiv.fetch()
    except Exception as e:
        print(f"[run_all] fetch_arxiv crashed: {e}")
    try:
        fetch_hf.fetch()
    except Exception as e:
        print(f"[run_all] fetch_hf crashed: {e}")
    analyze.main()
    render.main()
    rankings.main()


if __name__ == "__main__":
    main()
