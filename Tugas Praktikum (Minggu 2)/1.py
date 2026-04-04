import timeit
import random

# 1. Analisis Dua Fungsi

# Fungsi A:
def akses_langsung(data):
    duplikat = []
    n = len(data)
    for i in range(n):
        for j in range(i + 1, n):
            if data[i] == data[j] and data[i] not in duplikat:
                duplikat.append(data[i])
    return duplikat

# Fungsi B:
def cari_manual(data):
    terlihat = set()
    duplikat = set()
    for angka in data:
        if angka in terlihat:
            duplikat.add(angka)
        else:
            terlihat.add(angka)
    return list(duplikat)

# 2. Uji Penetrasi

ukuran_n = [100, 1000, 10000]

print("Mulai Pengujian Waktu Eksekusi (10 iterasi per ukuran data)...\n")
print("-" * 67)
print(f"{'Ukuran Data (n)':<20} | {'Fungsi A O(n^2)':<15}      | {'Fungsi B O(n)':<15}")
print("-" * 67)

for n in ukuran_n:
    data_uji = [random.randint(1, n // 2) for _ in range(n)]
    waktu_A = timeit.timeit(lambda: akses_langsung(data_uji), number=10)
    waktu_B = timeit.timeit(lambda: cari_manual(data_uji), number=10)
    print(f"{n:<20} | {waktu_A:<15.5f}detik | {waktu_B:<15.5f}detik")

print("-" * 67)
