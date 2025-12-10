from typing import List

import requests

from .types import ScanResult, STATUS_CODES
from .utils import progress_bar


def get_status_code(url: str) -> int:
    try:
        response = requests.get(url, timeout=5)
        return response.status_code
    except requests.RequestException:
        return -1


def scan_url(url: str, word_lists: List[str], extensions: List[str] = None) -> List[ScanResult]:
    confirmed = []

    for word in progress_bar(word_lists, desc="Nge-dowse URL..."):
        send_to = f"{url.rstrip('/')}/{word}"
        status_code = get_status_code(send_to)

        if status_code in STATUS_CODES:
            confirmed.append(ScanResult(send_to, status_code))

        if extensions is not None:
            for ext in extensions:
                send_to_ext = f"{send_to}{ext}"
                status_code_ext = get_status_code(send_to_ext)

                if status_code_ext in STATUS_CODES:
                    confirmed.append(ScanResult(send_to_ext, status_code_ext))

    return confirmed