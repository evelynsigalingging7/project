def menghitung_bmr(): # fungsi untuk menghitung BMR
    print("---MASUKAN DATA ANDA---")
    print()
    berat = float(input("Masukkan berat badan Anda (kg): "))
    tinggi = float(input("Masukkan tinggi badan Anda (cm): "))
    usia = int(input("Masukkan usia Anda (tahun): "))
    jenis_kelamin = input("Masukkan jenis kelamin Anda (L/P): ").strip().upper()#srip dan upper untuk menghilangkan spasi dan mengubah ke huruf besar

    if jenis_kelamin == 'L':
        bmr = 88.362 + (13.397 * berat) + (4.799 * tinggi) - (5.677 * usia)
    elif jenis_kelamin == 'P':
        bmr = 447.593 + (9.247 * berat) + (3.098 * tinggi) - (4.330 * usia)
    else:
        print("Jenis kelamin tidak valid.")
        return None #untuk mengembalikan nilai bmr
    print()
    print(f"BMR Anda adalah: {bmr:.2f} kalori/hari")
    return bmr

def aktivitas():# fungsi untuk menentukan faktor aktivitas
    while True:
        print("\nPilih tingkat aktivitas fisik Anda:")
        print("1. Tidak aktif (sedikit atau tidak ada olahraga)")
        print("2. Sedikit aktif (olahraga ringan/sedang 1-3 hari/minggu)")
        print("3. Cukup aktif (olahraga sedang 3-5 hari/minggu)")
        print("4. Sangat aktif (olahraga berat 6-7 hari/minggu)")
        print("5. Ekstra aktif (pekerjaan fisik berat atau latihan dua kali sehari)")

        pilihan = int(input("Masukkan pilihan Anda (1-5): "))#mengambil input dari user
# menentukan faktor aktivitas berdasarkan pilihan user setiap pilihan akan dikalikan dengan faktor dari masing-masing pilihan
        if pilihan == 1:
            faktor = 1.2
        elif pilihan == 2:
            faktor = 1.375
        elif pilihan == 3:
            faktor = 1.55
        elif pilihan == 4:
            faktor = 1.725
        elif pilihan == 5:
            faktor = 1.9
        else:
            print("PILIHAN TIDAK VALID. Silakan coba lagi.")
            continue
        return faktor#mengembalikan nilai faktor aktivitas

def main():# ini adalah fungsi utama dari program yang menggabungkan semua fungsi dari program ini
    print("----SELAMAT DATANG DI PROGRAM MENGHITUNG KALORI HARIAN!----")
    print()
    bmr = menghitung_bmr()#variabel bmr untuk menyimpan nilai dari fungsi menghitung_bmr
    if bmr is None:#jika bmr tidak bernilai maka program akan kembali ke menu fungsi utama
        return
    faktor_aktivitas = aktivitas()#variabel faktor_aktivitas untuk menyimpan nilai dari fungsi aktivitas
    kebutuhan_kalori = bmr * faktor_aktivitas#kebutuhan_kalori dihitung dengan mengalikan bmr dengan faktor_aktivitas
    print(f"\nKebutuhan kalori harian Anda adalah: {kebutuhan_kalori:.2f} kalori/hari")
    #menampilkan kebutuhan kalori harian dan .2f untuk membatasi 2 angka di belakang koma

def menghitung_kalori_harian():#fungsi ini untuk menghitung kalori dari makanan yang kita konsumsi dalam satu hari
    print("\n---Menghitung Kalori dari Makanan yang Dikonsumsi---")
    print("---nasi---\n---ayam goreng---\n---sayur---\n---buah---\n---susu---")#menampilkan pilihan makanan yang tersedia
    print("contoh: nasi,ayam goreng,sayur")
    masukan_makanan = input("Masukkan makanan yang Anda konsumsi hari ini: ")#MENGAMBIL DATA DARI USER DAN USER MEMASUKAN NAMA MAKANAN YANG DIKONSUMSI
    kalori_per_makanan = {#dictionary untuk menyimpan kalori dari setiap makanan, karena setiap nama makanan terdapat value kalori
        "nasi": 200,
        "ayam goreng": 300,
        "sayur": 50,
        "buah": 80,
        "susu": 150
    }
    total_kalori = 0 #total kalori untuk menyimpan nilai kalori yang dikonsumsi
    makanan_list = masukan_makanan.lower().split(',')
    #variabel makanan_list untuk mentimpan makanan yang dimasukan user,fungsi lower untuk mengubah huruf besar jadi kecil 
    # dan split untuk memisahan makanan dengan koma
    for makanan in kalori_per_makanan:#melakukan perulangan untuk makanan yang ada di dictionary kalori_per_makanan
        if makanan in makanan_list: #kalau makanan ada di dalam makanan_list maka kalori makanan akan ditambahkan ke total_kalori
            total_kalori += kalori_per_makanan[makanan]#ini untuk menambahkan total_kalori dengan kalori makanan yang diinput di makanan_list
            #kalori_per_makanan[makanan] mengambil nilai dari dictionary sesuai yang diinput user 
            print(f"kalori dari {makanan}:{kalori_per_makanan[makanan]} kalori")
            #ini menampilkan makanan dan niali kalorinya dalam makanan yang diinput user
    print(f"Total kalori yang Anda konsumsi hari ini: {total_kalori} kalori")
    #ini menampilkan keseluruhan kalori yang dikonsumsi dalam sehari

def perulangan(): # def perulangan ini untuk mengulang semua program jika user ingin menghitung lagi
    while True:
        ulang = input("\nApakah Anda ingin menghitung lagi? (y/n): ").lower()#menggunakan fungsi lower karena jika user mengimput dengan angka besar akan diubah oleh lower menjadi kecil
        if ulang == 'y':#jika y program diulang
            return True#maka akan mengembalikan nilai True
        elif ulang == 'n':
            print("Terima kasih telah menggunakan program ini. Sampai jumpa!")
            return False#jika n program berhenti atau break
        else:
            print("PILIHAN TIDAK BENAR!. Silakan masukkan 'y' atau 'n'.")
            # continue looping until valid input

while True:
    main()
    menghitung_kalori_harian()
    if not perulangan():
        break
    