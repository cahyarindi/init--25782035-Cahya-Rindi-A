"""
Nama File: check_number.py

Tujuan Program:
Memeriksa apakah suatu nilai berada dalam rentang tertentu.

Fitur Utama:
1. Memvalidasi bahwa nilai tidak bernilai None
2. Memeriksa apakah nilai lebih besar dari 0
3. Memeriksa apakah nilai kurang dari 100

Penulis:
(Nama Anda)

Tanggal Pembaruan Terakhir:
2026-03-11
"""


def check(n):
    """
    Periksa apakah nilai berada dalam rentang 1 sampai 99.

    Parameter:
    n (int | None): Nilai yang akan diperiksa.

    Nilai Kembalian:
    bool: True jika nilai tidak None, lebih besar dari 0,
    dan kurang dari 100. False jika tidak memenuhi syarat.

    Contoh:
    >>> check(50)
    True
    >>> check(-5)
    False
    >>> check(None)
    False
    """
    if n is not None:
        if n > 0:
            if n < 100:
                return True
    return False


print(check(50))