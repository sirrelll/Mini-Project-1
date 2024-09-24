umur = int(input("Masukkan Umur: "))

if umur >= 35 and umur <= 40:
    print("..........")
    if umur >= 60:
        print("Selamat Siang Kaik/Nenek")
    elif umur >= 33:
        print("Selamat Siang Pak/Buk")
elif umur >= 20:
    print("Selamat Siang Bang/Mba")
elif umur >= 1:
    print("Selamat Siang Dek")