# Nazrin

Tool untuk mencari path/hidden dir di sebuah website dengan memakai wordlist.

Dibuat untuk memenuhi soal tes penerimaan magang di Cyber Army Indonesia.

Sengaja dibikin semodular mungkin + pakai type annotations. Buat menunjukkan
kalau nanti saya bisa bikin kode seperti ini lagi buat task yang kompleks pas magang.

Nama diambil dari karakter game Touhou yang suka dowsing (cocok, toolnya buat nyari hidden URL).

## Data Diri

Nama: Rahman Hakim (607062330006)

Kampus: Telkom University

Fakultas: Fakultas Ilmu Terapan

Prodi: D3 RPLA

## Contoh Penggunaan

```bash
usage: main.py [-h] --url URL --wordlist WORDLIST [--threads THREADS] [--extensions EXTENSIONS [EXTENSIONS ...]]

Scan semua hidden dir di url

options:
  -h, --help            show this help message and exit
  --url URL             URL yang akan di-scan
  --wordlist WORDLIST   Path ke wordlist yang mau dipakai
  --threads THREADS     Jumlah threads yang mau dipakai (default: 1)
  --extensions EXTENSIONS [EXTENSIONS ...]
                        Extensions tambahan yang mau di-scan (contoh: .php, .txt)
```

Penggunaan ke website saya (https://kakashispiritnews.my.id/) pakai wordlist yang ada di wordlists/wordlist.txt.

```bash
python3 main.py --url https://kakashispiritnews.my.id/ --wordlist wordlists/wordlist.txt --extensions .xml + .html --threads=5
```

Saya pakai ke website pribadi. Threadsnya 5, karena wordlistnya ada 10, tiap thread bakal proses 2 words.

### Output
```
Nazrin mulai!
Nge-dowse hidden path/dir di https://kakashispiritnews.my.id/ pakai 5 thread...
Wordlist: wordlists/wordlist.txt...
Nge-dowse URL...: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 2/2 [00:00<00:00,  2.07it/s]
Nge-dowse URL...: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 2/2 [00:00<00:00,  2.06it/s]
Nge-dowse URL...: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 2/2 [00:00<00:00,  2.05it/s]
Nge-dowse URL...: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 2/2 [00:00<00:00,  2.03it/s]
Nge-dowse URL...: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 2/2 [00:00<00:00,  2.03it/s]
Nge-dowse URL...: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 2/2 [00:00<00:00,  2.06it/s]
Done. Hasilnya disimpan di result.txt███████████████████████████████████████████████████████████████████████████████████████████████████| 2/2 [00:00<00:00,  2.07it/s]
[+] Found:  https://kakashispiritnews.my.id/about (200)█████████████████████████████████████████████████████████████████████████████████| 2/2 [00:00<00:00,  2.04it/s]
[+] Found:  https://kakashispiritnews.my.id/Bermain-Touhou-di-Linux.html (200)
[+] Found:  https://kakashispiritnews.my.id/sitemap.xml (200)
[+] Found:  https://kakashispiritnews.my.id/Bermain-Touhou-di-Linux (200)
[+] Found:  https://kakashispiritnews.my.id/sitemap (200)
[+] Found:  https://kakashispiritnews.my.id/categories.html (200)
[+] Found:  https://kakashispiritnews.my.id/index (200)
[+] Found:  https://kakashispiritnews.my.id/about.html (200)
[+] Found:  https://kakashispiritnews.my.id/index.html (200)
[+] Found:  https://kakashispiritnews.my.id/categories (200)
```

## Instalasi

- Clone.
- Run `pip install -r requirements.txt`.
- Run script di contoh.



