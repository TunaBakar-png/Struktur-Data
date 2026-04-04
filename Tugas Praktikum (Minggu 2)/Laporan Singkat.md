## 1. Tabel Perbandingan Waktu Eksekusi
*(Catatan: Waktu di bawah adalah total untuk 10 kali eksekusi (detik). Angka pasti akan berbeda tergantung spesifikasi perangkat).*

| Ukuran Data (n) | Waktu Fungsi A $O(n^2)$ | Waktu Fungsi B $O(n)$ |
| :--- | :--- | :--- |
| 100 | 0.00160 detik | 0.00006 detik |
| 1.000 | 0.18398 detik | 0.00056 detik |
| 10.000 | 17.78333 detik |  0.00697 detik |

## 2. Mengapa Fungsi B Jauh Lebih Cepat Daripada Fungsi A?

Berdasarkan data uji penetrasi di atas, terlihat jelas bahwa Fungsi B jauh lebih cepat dibandingkan Fungsi A, terutama saat ukuran data `n` semakin membesar (misalnya dari 1.000 ke 10.000). 

Hal ini terjadi karena perbedaan **Kompleksitas Waktu (Big-O)** pada algoritma yang digunakan:

* **Fungsi A memiliki kompleksitas $O(n^2)$**: Fungsi ini menggunakan metode *nested loop* (perulangan di dalam perulangan). Jika data berisi 10.000 elemen, loop luar berjalan 10.000 kali dan loop dalam juga berjalan hingga 10.000 kali. Artinya, komputer berpotensi melakukan hingga 100.000.000 operasi pengecekan. Waktu eksekusinya meningkat secara kuadratik, sehingga sangat lambat untuk data besar.
* **Fungsi B memiliki kompleksitas $O(n)$**: Fungsi ini menggunakan struktur data `set` yang memanfaatkan metode pencarian *Hash Table*. Operasi pengecekan `if angka in terlihat` pada Set membutuhkan waktu konstan. Karena hanya ada satu perulangan tunggal, jumlah operasi akan berbanding lurus dengan jumlah elemen (10.000 elemen = $\pm$ 10.000 operasi). Pertumbuhannya linier, sehingga eksekusinya sangat efisien dan memakan waktu jauh lebih singkat.