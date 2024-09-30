# Mini Project 1
Nama : Darel Prasetya Fawwaz, NIM : 2409116064, Nama Tugas :...

Penjelasan:
1. Baris 6-9 merupakan cara untuk memunculkan login sederhana serta menginput data seperti Nama, NIM, dan Kelas.
print("-----LOGIN-----")
nama =  input("Masukkan Nama: ")
nim =   input("Masukkan NIM: ")
kelas = input("Masukkan Kelas: ")

2. Baris 12-14 untuk memunculkan hasil login sederhana setelah memasukkan Nama, NIM, Kelas.
print("\nSelamat anda telah berhasil login,", nama)
print("NIM: ", nim)
print("Kelas: ", kelas)

3. Baris 17-21 membuat daftar barang beserta harganya untuk ditampilkan
barang = {
    "Baju":150000,
    "Celana":250000,
    "Tas":200000,
}

4. Baris 24-27 untuk menampilkan daftar barang yang telah dibuat pada baris sebelumnya.
   dengan adanya "for a in barang" kita bisa mengambil data yang ada di baris 17-21 dan dengan adanya "\t" akan membuat spasi
   pada setiap barang yang ada pada daftar.
print("----------------------DAFTAR BARANG-----------------------")
for a in barang:
    print("Daftar Barang:", a,"\t Harga :", barang[a])
print("--------------------------------------------------------")

5. Baris 32-36 
while True:
            pilih_barang = input("Barang yang dipesan: ",)
            jumlah_pembelian = int(input("Jumlah Pesanan: "))
            
            total_harga = jumlah_pembelian * barang[pilih_barang]
