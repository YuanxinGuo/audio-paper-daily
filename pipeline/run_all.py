"""End-to-end runner: fetch -> analyze -> render -> rankings."""
import fetch_arxiv
import fetch_hf
import analyze
import render
import rankings


def main() -> None:
    fetch_arxiv.fetch()
    fetch_hf.fetch()
    analyze.main()
    render.main()
    rankings.main()


if __name__ == "__main__":
    main()
