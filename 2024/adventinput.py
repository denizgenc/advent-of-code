import os
import ssl
import sys
from pathlib import Path
from typing import List
import urllib.request

CACHE_DIR = Path.cwd() / ".inputcache"

def get_data(advent_day: int) -> List[str]:
    cache_path = CACHE_DIR / f"day_{advent_day}.txt"
    if cache_path.is_file():
        with open(cache_path) as f:
            return [line.strip() for line in f.readlines()]

    if not CACHE_DIR.is_dir():
        CACHE_DIR.mkdir()

    return download_input(advent_day, cache_path)

def download_input(advent_day: int, cache_path: Path) -> List[str]:
    cookie = get_cookie()
    header = {
        "Cookie": f"session={cookie}",
    }

    request = urllib.request.Request(
        f"https://adventofcode.com/2024/day/{advent_day}/input", headers=header
    )

    lines = []
    with urllib.request.urlopen(request, context=ssl.create_default_context()) as data:
        with open(cache_path, "wb") as f:
            for line in data:
                f.write(line)
                lines.append(str(line, encoding="utf-8").strip())
    return lines

def get_cookie():
    try:
        return os.environ["ADVENT_COOKIE"]
    except KeyError:
        print("ADVENT_COOKIE environment variable not set", sys.stderr)
        exit(1)
