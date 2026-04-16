angka = input("masukkan angka:")
a,b,c = map(int,angka.split(","))
if a > b and a > c:
    terbesar= a
elif b > a and b > c:
    terbesar = b
else:
    terbesar = c
print("angka terbesar:",terbesar)
