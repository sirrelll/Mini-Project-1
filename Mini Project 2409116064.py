# inputan login
print("-----LOGIN-----")
nama =  input("Masukkan Nama: ")
nim =   input("Masukkan NIM: ")
kelas = input("Masukkan Kelas: ")

print("\nSelamat anda telah berhasil login,", nama)
print("NIM: ", nim)
print("Kelas: ", kelas)

# membuat daftar barang
barang = {
    "Baju":150000,
    "Celana":250000,
    "Tas":200000,
}
print("----------------------DAFTAR BARANG-----------------------")
for a in barang:
    print("Daftar Barang:", a,"\t Harga :", barang[a])
print("--------------------------------------------------------")

#menginput barang
while True:
            pilih_barang = input("Barang yang dipesan: ",)
            jumlah_pembelian = int(input("Jumlah Pesanan: "))
            
            total_harga = jumlah_pembelian * barang[pilih_barang]

# menentukan diskon
            if total_harga > 250000:
                diskon = total_harga*25/100
                total = total_harga - diskon
                print("\nSelamat anda mendapatkan diskon sebesar 25%")
            else:
                total = total_harga 

            print("----------------Pembayaran----------------")
            print("Barang yang dipesan      : ", pilih_barang)
            print("Jumlah yang dipesan      : ", jumlah_pembelian)
            print("Total biaya              : ", total_harga)
            print("Total yang harus dibayar : ", total)
            print("------------------------------------------")

# mengulang
            ulang = input("Apakah ingin menghitung ulang? (yes/no) : ").lower()
            if ulang != 'yes':
                print("Terima kasih telah berbelanja disini")
                break
