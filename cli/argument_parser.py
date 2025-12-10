import argparse


def create_argument_parser():
    parser = argparse.ArgumentParser(description="Scan semua hidden dir di url")

    parser.add_argument(
        "--url",
        type=str,
        required=True,
        help="URL yang akan di-scan"
    )
    parser.add_argument(
        "--wordlist",
        type=str,
        required=True,
        help="Path ke wordlist yang mau dipakai"
    )
    parser.add_argument(
        "--threads",
        type=int,
        default=1,
        help="Jumlah threads yang mau dipakai (default: 1)"
    )
    parser.add_argument(
        "--extensions",
        type=str,
        nargs="+",
        help="Extensions tambahan yang mau di-scan (contoh: .php, .txt)"
    )

    return parser