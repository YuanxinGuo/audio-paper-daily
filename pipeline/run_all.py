"""End-to-end runner: fetch -> analyze -> render -> rankings -> home."""
import fetch_arxiv
import analyze
import render
import rankings
import home


def main() -> None:
    try:
        fetch_arxiv.fetch()
    except Exception as e:
        print(f"[run_all] fetch_arxiv crashed: {e}")
    analyze.main()
    render.main()
    rankings.main()
    home.main()


if __name__ == "__main__":
    main()
