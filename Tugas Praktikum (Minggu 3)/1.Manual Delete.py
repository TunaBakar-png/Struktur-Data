def manual_delete(arr, index,):
    n = len(arr)
    
    if index < 0 or index >= n:
        return "Error: Indeks di luar batas!"

    hasil = arr[:]

    for i in range(index, n - 1):
        hasil[i] = hasil[i + 1]
        
    hasil = hasil[:-1]
    
    return hasil

data_array = [10, 20, 30, 40, 50]
print(f"Data awal          : {data_array}")
print(f"Hapus indeks ke-2  : {manual_delete(data_array, 2)}")
print(f"Hapus indeks ke-0  : {manual_delete(data_array, 0)}")
print(f"Hapus indeks ke-10 : {manual_delete(data_array, 10)}")