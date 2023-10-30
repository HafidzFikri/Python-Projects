def luaslingkaran(bil1):
  bil1 = (bil1)
  if bil1 % 7 == 0:
    phi = 22/7
  else:
    phi = 3.14
  luas_lingkaran = phi * bil1**2
  return luas_lingkaran

def luaspersegi(bil1):
  luas_persegi = bil1**2
  return luas_persegi

def luaspersegipanjang(bil1,bil2):
  luas_persegipanjang = bil1 * bil2
  return luas_persegipanjang

def luassegitiga(bil1,bil2):
  luas_segitiga = 1/2 * bil1 * bil2
  return luas_segitiga

def volumebola(bil1):
  bil1 = (bil1)
  if bil1 % 7 == 0:
    phi = 22/7
  else:
    phi = 3.14
  volume_lingkaran = 4/3 * phi * bil1**3
  return volume_lingkaran

def volumekubus(bil1):
  volume_kubus = bil1**3
  return volume_kubus

def volumebalok(bil1,bil2,bil3):
  volume_balok = bil1 * bil2 * bil3
  return volume_balok


while True:
   print("Pilihlah operasi yang ingin dilakukan!\n"
  "1. Luas Lingkaran \n"
  "2. Luas Persegi \n"
  "3. Luas Persegi Panjang \n"
  "4. Luas Segitiga \n\n"
  "5. Volume Bola \n"
  "6. Volume Kubus \n"
  "7. Volume Balok \n"
  "8. Volume Kerucut \n"
  "9. Volume Prisma Segitiga \n"
  "10. Volume Limas Segitiga \n"
  "11. Volume Limas Segiempat \n"
        )
    pilihan = int(input("Pilihlah operasi yang ingin dilakukan: "))
    if pilihan == 1:
        print("\nAnda memilih operasi LUAS LINGKARAN")
        bil1 = int(input("Masukkan Radius: "))
        hasil = luaslingkaran(bil1)
        print("Luas lingkaran =", hasil)

    elif pilihan == 2:
        print("\nAnda memilih operasi LUAS PERSEGI")
        bil1 = int(input("Masukkan panjang sisi: "))
        hasil = luaspersegi(bil1)
        print("Luas Persegi =", hasil)

    elif pilihan == 3:
        print("\nAnda memilih operasi LUAS PERSEGI PANJANG")
        bil1 = int(input("Masukkan panjang: "))
        bil2 = int(input("Masukkan lebar: "))
        hasil = luaspersegipanjang(bil1,bil2)
        print("Luas Persegi Panjang =", hasil)

    elif pilihan == 4:
        print("\nAnda memilih operasi LUAS SEGITIGA")
        bil1 = int(input("Masukkan Alas : "))
        bil2 = int(input("Masukkan Tinggi : "))
        hasil = luassegitiga(bil1,bil2)
        print("Luas Segitiga =", hasil)

    elif pilihan == 5:
        print("\nAnda memilih operasi VOLUME BOLA")
        bil1 = int(input("Masukkan radius : "))
        hasil = volumebola(bil1)
        print("Volume Bola =", hasil)

    elif pilihan == 6:
        print("\nAnda memilih operasi VOLUME KUBUS")
        bil1 = int(input("Masukkan panjang sisi: "))
        hasil = volumekubus(bil1)
        print("Volume Kubus =", hasil)

    elif pilihan == 7:
        print("\nAnda memilih operasi VOLUME BALOK")
        bil1 = int(input("Masukkan panjang: "))
        bil2 = int(input("Masukkan lebar: "))
        bil3 = int(input("Masukkan tinggi: "))
        hasil = volumebalok(bil1,bil2,bil3)
        print("Volume Balok =", hasil)

    elif pilihan == 8:
        print("\nAnda memilih operasi VOLUME KERUCUT")
        print("  ! NOTE: Apabila telah diketahui Luas Alas makan isi radius dengan (0) !")
        bil1 = int(input("Masukkan radius: "))
        if bil1 == 0:
            bil4 = int(input("Masukkan Luas Alas : "))
        bil2 = int(input("Masukkan tinggi: "))
        hasil = luaslingkaran(bil1) * bil2
        if hasil == 0:
            hasil = bil4 * bil2
        print("Volume Kerucut =", hasil)

    elif pilihan == 9:
        print("\nAnda memilih operasi VOLUME PRISMA SEGITIGA")
        print("  ! NOTE: Apabila telah diketahui Luas Alas makan isi panjang sisi alas dengan (0) !")
        bil1 = int(input("Masukkan panjang sisi alas: "))
        if bil1 == 0:
            bil4 = int(input("Masukkan Luas Alas : "))
        else:
            bil2 = int(input("Masukkan lebar/tinggi sisi alas: "))
        bil3 = int(input("Masukkan tinggi prisma: "))
        hasil = luassegitiga(bil1,bil2) * bil3
        if hasil == 0:
            hasil = bil4 * bil3
        print("Volume Prisma Segitiga =", hasil)

    elif pilihan == 10:
        print("\nAnda memilih operasi VOLUME LIMAS SEGITIGA")
        print("  ! NOTE: Apabila telah diketahui Luas Alas makan isi panjang sisi alas dengan (0) !")
        bil1 = int(input("Masukkan panjang sisi alas: "))
        if bil1 == 0:
            bil4 = int(input("Masukkan Luas Alas : "))
        else:
            bil2 = int(input("Masukkan lebar/tinggi sisi alas: "))
        bil3 = int(input("Masukkan tinggi limas: "))
        hasil = luassegitiga(bil1,bil2) * bil3
        if hasil == 0:
            hasil = bil4 * bil3
        print("Volume Limas Segitiga =", hasil)

    elif pilihan == 11:
        print("\nAnda memilih operasi VOLUME LIMAS SEGIEMPAT")
        print("  ! NOTE: Apabila telah diketahui Luas Alas makan isi panjang sisi alas dengan (0) !")
        bil1 = int(input("Masukkan panjang sisi alas: "))
        if bil1 == 0:
            bil4 = int(input("Masukkan Luas Alas : "))
        else:
            bil2 = int(input("Masukkan lebar sisi alas: "))
        bil3 = int(input("Masukkan tinggi limas: "))
        hasil = luaspersegipanjang(bil1,bil2) * bil3
        if hasil == 0:
            hasil = bil4 * bil3
        print("Volume Limas Segiempat =", hasil)
    else:
        print("cuy")
    ulangi = input("\nApakah ingin mencoba lagi? (ya/no) :")
    if ulangi.lower() != "ya":
        break
print("Terimakasih Telah Menggunakan Program Kami :)")