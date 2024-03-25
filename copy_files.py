import argparse
import shutil
from pathlib import Path


def parse_argv():
    parser = argparse.ArgumentParser("Sort files")
    parser.add_argument(
        "-S", "--source", type=Path, required=True, help="Source folder"
    )
    parser.add_argument(
        "-O",
        "--output",
        type=Path,
        default=Path("output"),
        help="Output folder",
    )
    return parser.parse_args()


def recursive_copy(src: Path, dist: Path):
    if not src.exists():
        print(f"{src} does not exist")
        return

    try:
        for item in src.iterdir():
            if item.is_dir():
                recursive_copy(item, dist)
            else:
                suffix = item.suffix
                folder = dist / suffix[1:] if suffix else 'other'

                try:
                    folder.mkdir(exist_ok=True, parents=True)
                    shutil.copy2(item, folder)
                except:
                    print(f"Failed to copy file {item}")
    except:
        print(f"No access to {src}")


def main():
    args = parse_argv()
    recursive_copy(args.source, args.output)
    print("Process finished")


if __name__ == "__main__":
    main()
