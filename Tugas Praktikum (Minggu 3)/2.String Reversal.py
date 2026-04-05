def manual_reverse(teks):
    teks_terbalik = ""
    n = len(teks)
    
    for i in range(n - 1, -1, -1):
        teks_terbalik += teks[i]
        
    return teks_terbalik

kalimat_asli = "Did You Forget Your Own Homeland"
print(f"Kalimat Asli       : '{kalimat_asli}'")
print(f"Kalimat Terbalik   : '{manual_reverse(kalimat_asli)}'")
