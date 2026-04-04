import sys

angka_sederhana = 10

list_angka = [10]

memori_integer = sys.getsizeof(angka_sederhana)
memori_list = sys.getsizeof(list_angka)

print(f"Data Integer : {angka_sederhana}")
print(f"Ukuran Memori Integer: {memori_integer} bytes\n")

print(f"Data List    : {list_angka}")
print(f"Ukuran Memori List   : {memori_list} bytes\n")

print(f"Selisih Memori       : {memori_list - memori_integer} bytes")