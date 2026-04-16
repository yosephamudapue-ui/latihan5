nilai= int(input("masukkan nilai:"))
if nilai  > 75:
    print("lulus")
elif nilai >= 50:
    print("tidak lulus")
elif  nilai <50:
    print("perbaikan")

nilai = int(input("masukkan nilai:"))
absensi = int(input("masukkan absensi:"))
if nilai >70 and absensi >50:
 print("lulus")
elif (nilai >70 and absensi <70) or (nilai >70 and absensi <50):
 print("perbaikan")
else : 
 print("tidak lulus dan tidak bisa perbaikan")
