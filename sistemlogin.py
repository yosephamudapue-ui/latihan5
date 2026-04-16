password_benar = "kerin1508"

percobaan1 = input("Masukkan password: ")
if percobaan1 == password_benar:
    print("Login berhasil")

else:
    print("Password salah! Sisa percobaan: 2")
    percobaan2 = input("Masukkan password: ")
    if percobaan2 == password_benar:
        print("Login berhasil")

    else:
        print("Password salah! Sisa percobaan: 1")
        percobaan3 = input("Masukkan password: ")
        if percobaan3 == password_benar:
            print("Login berhasil")
        else:
            print("Akun terkunci Sudah 3x salah.")
