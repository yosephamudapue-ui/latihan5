masa_kerja = int(input("Masukkan masa kerja (tahun): "))
performa = input("Masukkan performa (baik/kurang): ").lower()

if masa_kerja >= 5 and performa == "baik":
    print("Bonus besar")
elif masa_kerja >= 5 or performa == "baik":
    print("Bonus kecil")
else:
    print("Tanpa bonus")
