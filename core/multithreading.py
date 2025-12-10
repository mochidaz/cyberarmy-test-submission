import threading
from typing import List, Callable, Any

from .utils import chunk_list


def run_parallel(target_func: Callable[[Any], Any], data_list: List[str], thread_count: int = 10):
    # Awalnya agak bingung concurrencynya mau dipakai untuk apa di satu URL.
    # Sempet bikin si argument parser bisa nerima lebih dari 1 URL.
    # Tapi karena tasknya adalah untuk 1 website, jadi akhirnya dipakai untuk nge-split si wordlist.

    real_thread_count = min(thread_count, len(data_list))
    chunks = chunk_list(data_list, real_thread_count)

    results = []
    threads = []
    lock = threading.Lock()

    def worker_wrapper(chunk_data):
        output = target_func(chunk_data)
        if output:
            with lock:
                results.extend(output)

    for chunk in chunks:
        t = threading.Thread(target=worker_wrapper, args=(chunk,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    return list(set(results))