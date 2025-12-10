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

## Instalasi

- Clone.
- Run `pip install -r requirements.txt`.
- Run script di contoh.



