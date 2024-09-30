# Mini Project 1
Nama : Darel Prasetya Fawwaz, NIM : 2409116064, Nama Tugas : Mini Project 1 (NIM Genap)

Flowchart draw.io
![Mini Project 2409116064  drawio](https://github.com/user-attachments/assets/759c7e80-f130-41a4-a9fc-a9d48f8410fe)
Penjelasan tentang Flowchart draw.io
Tentunya diawali dengan simbol start, yang kemudian dilanjutkan dengan simbol data untuk menginput Namma, NIM, beserta Kelas, setelah itu
munculkan simbol process untuk menampilkan pesan yaitu "Selamat anda telah berhasil login" tampilkan lagi simbol process untuk menampilkan daftar barang beserta harganya, dan munculkan simbol data untuk menginput harga dan jumlah yang kita inginkan, munculkan simbol decision yang dimana jika harga melebihi 250.000 maka total harga akan mendapatkan diskon sebesar 25% dan jika harga kurang dari atau sama dengan 250.000 maka total harga akan tetap, kemudian munculkan simbol process untuk menampilkan pembayaran yang sudah ditetapkan, munculkan simbol decision apakah ingin menghitung ulang atau tidak, jika iya maka akan dikembalikan ke input harga dan jumlah dan jika tidak maka keluar dari program.

Program Python Mini Project 1 (NIM Genap)
![Program Python Mini Project 1](https://github.com/user-attachments/assets/8b0d7675-468d-4b3b-b0fe-ccb8ec841a6b)
Penjelasan:
1. Baris 6-9 merupakan cara untuk memunculkan login sederhana serta menginput data seperti Nama, NIM, dan Kelas.


   print("-----LOGIN-----")
   nama =  input("Masukkan Nama: ")
   nim =   input("Masukkan NIM: ")
   kelas = input("Masukkan Kelas: ")

1. Baris 12-14 untuk memunculkan hasil login sederhana setelah memasukkan Nama, NIM, Kelas.

   
   print("\nSelamat anda telah berhasil login,", nama)
   print("NIM: ", nim)
   print("Kelas: ", kelas)

4. Baris 17-21 membuat daftar barang beserta harganya untuk ditampilkan.

   
   barang = {
       "Baju":150000,
       "Celana":250000,
       "Tas":200000,
   }

6. Baris 24-27 untuk menampilkan daftar barang yang telah dibuat pada baris sebelumnya.
   dengan adanya "for a in barang" kita bisa mengambil data yang ada di baris 17-21 dan dengan adanya "\t" akan membuat spasi
   pada setiap barang yang ada pada daftar.

   
   print("----------------------DAFTAR BARANG-----------------------")
   for a in barang:
       print("Daftar Barang:", a,"\t Harga :", barang[a])
   print("--------------------------------------------------------")

8. Baris 32-36 untuk menginput barang beserta jumlahnya agar bisa menghitung total harga barang yang telah diinputkan.

   
   while True:
               pilih_barang = input("Barang yang dipesan: ",)
               jumlah_pembelian = int(input("Jumlah Pesanan: "))
               total_harga = jumlah_pembelian * barang[pilih_barang]

10. Baris 43-48 untuk menentukan jika total harga melebihi 250.000 maka akan mendapatkan diskon sebesar 25% dan jika total harga tidak melebihi 250.000
   maka total harga akan tetap.


   if total_harga > 250000:
                diskon = total_harga*25/100
                total = total_harga - diskon
                print("\nSelamat anda mendapatkan diskon sebesar 25%")
            else:
                total = total_harga 

12. Baris 52-57 untuk menampilkan data pada baris 43-48 sehingga muncullah data pembayaran yang telah diinputkan pada baris sebelumnya.

    
            print("----------------Pembayaran----------------")
            print("Barang yang dipesan      : ", pilih_barang)
            print("Jumlah yang dipesan      : ", jumlah_pembelian)
            print("Total biaya              : ", total_harga)
            print("Total yang harus dibayar : ", total)
            print("------------------------------------------")

14. Baris 60-63 untuk memunculkan perulangan yang memberikan piiihan apakah ingin menghitung total harga kembali atau
   keluar dari program ini.


               ulang = input("Apakah ingin menghitung ulang? (yes/no) : ").lower()
            if ulang != 'yes':
                print("Terima kasih telah berbelanja disini")
                break
