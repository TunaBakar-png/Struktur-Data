## 1. Analisis Operasi Pergeseran pada Array (Manual Delete)

Pada fungsi `manual_delete(arr, index)`, proses penghapusan dilakukan dengan menggeser elemen di sebelah kanan indeks ke arah kiri. Jumlah operasi pergeseran ini sangat bergantung pada posisi indeks elemen yang dihapus:

* **Menghapus Elemen Pertama (Indeks 0) -> Kompleksitas $O(n)$**
  Menghapus elemen paling depan, maka **seluruh elemen sisanya** di sebelah kanan (sebanyak $n-1$ elemen) harus digeser ke kiri satu per satu. Pada kasus terburuk, jumlah pergeseran sebanding dengan jumlah data ($n$). Oleh karena itu, kompleksitas waktunya adalah $O(n)$.

* **Menghapus Elemen Terakhir (Indeks n-1) -> Kompleksitas $O(1)$**
  Menghapus elemen paling belakang, **tidak ada elemen di sebelah kanannya**. Artinya, loop pergeseran tidak akan berjalan sama sekali. Kita hanya perlu memotong satu slot di akhir array. Waktu eksekusinya selalu konstan, sehingga kompleksitas waktunya adalah $O(1)$.

## 2. Penjelasan Fungsi String Reversal

Fungsi `manual_reverse(teks)` membalikkan kalimat tanpa menggunakan fungsi bawaan seperti `[::-1]` atau `.reverse()`. 

**Kompleksitas Waktu:** $O(n)$
Fungsi ini menggunakan perulangan manual `for` yang berjalan dari indeks terakhir string hingga indeks pertama. Jika panjang string adalah $n$ karakter, maka perulangan akan dieksekusi tepat sebanyak $n$ kali untuk menyusun ulang string baru karakter demi karakter. Jadi, kompleksitas waktunya berjalan secara linier atau $O(n)$.