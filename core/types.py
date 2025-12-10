STATUS_CODES = [200, 301, 302]


class ScanResult:
    def __init__(self, url: str, status_code: int):
        self.url = url
        self.status_code = status_code

    def __repr__(self):
        return f"{self.url} ({self.status_code})"