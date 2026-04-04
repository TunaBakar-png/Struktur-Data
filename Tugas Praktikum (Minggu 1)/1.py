a = [1, 2, 3]
b = a

print(f"Sebelum diubah:")
print(f"List a: {a}")
print(f"List b: {b}\n")

a[0] = 11

print(f"Setelah List a diubah (a[0] = 11):")
print(f"List a: {a}")
print(f"List b: {b}\n")

print("Pengecekan Alamat Memori:")
print(f"Alamat memori a: {id(a)}")
print(f"Alamat memori b: {id(b)}")