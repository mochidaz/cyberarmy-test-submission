from cli.argument_parser import create_argument_parser
from core.multithreading import run_parallel
from core.scanner import scan_url
from core.utils import save_to_file, print_results, read_wordlist


def main():
    print("Nazrin mulai!")

    output_path = "result.txt" # Udah ada di default, tapi sengaja untuk ngeliatin flexiblity aja

    parser = create_argument_parser()

    args = parser.parse_args()

    rw = read_wordlist(args.wordlist)

    print(f"Nge-dowse hidden path/dir di {args.url} pakai {args.threads} thread...")
    print(f"Wordlist: {args.wordlist}...")

    worker = lambda chunk: scan_url(args.url, chunk, args.extensions)

    found = run_parallel(worker, rw, args.threads)

    if found:
        save_to_file(found, output_path)
        print(f"\nDone. Hasilnya disimpan di {output_path}")
        print_results(found)
    else:
        print("\nTidak ada path yang cocok di wordlist")


if __name__ == "__main__":
    main()