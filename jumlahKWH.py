KWH= int(input("masukkan jumlah KWH: "))
if KWH <= 100:
    biaya = KWH * 500
elif KWH <= 300:
    biaya = (100 * 500) + (KWH - 100) * 1000
else:
    biaya = (100 * 500) + (200 * 1000) + (KWH - 300) * 2000
print("total_biaya:",biaya)
 
