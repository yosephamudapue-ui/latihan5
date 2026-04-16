total_belanja = int(input("masukkan total belanja:"))

if total_belanja >= 500000:
    diskon = total_belanja* 0.2
elif total_belanja >= 300000:
    diskon = total_belanja * 0.1
elif total_belanja >= 100000:
    diskon = total_belanja* 0.05
else:
    diskon = 0

total_bayar = total_belanja - diskon
print("diskon:",diskon)
print("total bayar:",total_bayar)
