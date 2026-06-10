from pathlib import Path
import sys


def list_files_by_ext(directory: str, ext: str, recursive: bool = False) -> list[Path]:
    """
    List all files in a directory filtered by extension.

    Args:
        directory: Path to the directory to search
        ext:       File extension to filter by (with or without leading dot)
        recursive: If True, search subdirectories as well

    Returns:
        List of Path objects matching the extension

    Raises:
        NotADirectoryError: If the given path is not a valid directory
    """
    p = Path(directory)

    if not p.exists() or not p.is_dir():
        raise NotADirectoryError(f"'{directory}' is not a valid directory")

    if not ext.startswith("."):
        ext = "." + ext

    if recursive:
        return [f for f in p.rglob(f"*{ext}") if f.is_file()]
    else:
        return [f for f in p.iterdir() if f.is_file() and f.suffix == ext]


def display_files(files: list[Path], directory: str, ext: str) -> None:
    """Print a formatted table of files with their sizes."""
    if not files:
        print(f"No '{ext}' files found in {directory}")
        return

    print(f"\nFiles with {ext} extension in {directory}:")
    print("-" * 50)
    for f in files:
        size_kb = f.stat().st_size / 1024
        print(f"  {f.name:<35} {size_kb:>8.1f} KB")
    print("-" * 50)
    print(f"Total: {len(files)} file(s) found")


if __name__ == "__main__":
    # Configuration — change these as needed
    SEARCH_DIR = "/home/iamridoydey"
    EXTENSION  = "sh"
    RECURSIVE  = True

    try:
        files = list_files_by_ext(SEARCH_DIR, EXTENSION, recursive=RECURSIVE)
        print(files)
        display_files(files, SEARCH_DIR, EXTENSION)
    except NotADirectoryError as e:
        print(f"Error: {e}")
        sys.exit(1)