harga = float(input("masukkan total belanja:"))
if harga >= 100000:
    diskon = harga * 0.1
    total = harga - diskon
else:
    total = harga
print("total yang harus dibayar:",total)
