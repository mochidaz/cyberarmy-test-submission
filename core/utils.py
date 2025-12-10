import tqdm
import os

from pathlib import Path
from typing import List, Iterable, Any

from core.types import ScanResult


def read_wordlist(wordlist_path: Path) -> List[str]:
    words = None

    with open(wordlist_path, "r") as f:
        words = [line.strip() for line in f if line.strip()]

    return words


def save_to_file(output: List[ScanResult], filename: str = "result.txt") -> None:
    with open(filename, "w") as f:
        for line in output:
            f.write(line.__repr__() + os.linesep)


def progress_bar(iterable: Iterable[Any], desc: str):
    return tqdm.tqdm(iterable, desc=desc)


def print_results(results: List[ScanResult]) -> None:
    for result in results:
        print("[+] Found: ", result)


def chunk_list(data: List[str], num_chunks: int) -> List[List[str]]:
    if not data: return []
    avg = len(data) / float(num_chunks)
    out = []
    last = 0.0
    while last < len(data):
        out.append(data[int(last):int(last + avg)])
        last += avg
    return out