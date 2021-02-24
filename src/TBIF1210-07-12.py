import csv
#--------------------------------F01----------------------------------------------#
def load():
    # fungsi load merupakan prosedur yang digunakan untuk mengoutput variabel berupa array
    # variabel yang di output/ diglobalkan berupa
    # data_user, data_wahana, data_pembelian, data_penggunaan, data_tiket, data_refund, dan data_kritiksaran
    # Dan akan mengubah status login menjadi True
    
    # Kamus
    # file_user, file_wahana, file_pembelian, file_penggunaan, file_tiket, file_refund, dan file_kritiksaran : integer
    # data_user, data_wahana, data_pembelian, data_penggunaan, data_tiket, data_refund, dan data_kritiksaran : Array of string

    # Algoritma Prosedur
    global data_user
    global data_wahana
    global data_pembelian
    global data_penggunaan
    global data_tiket
    global data_refund
    global data_kritiksaran
    global data_tiket_hilang
    
    data_user=[0 for i in range (100)]
    data_wahana=[0 for i in range (100)]
    data_pembelian =[0 for i in range (100)]
    data_penggunaan=[0 for i in range (100)]
    data_tiket=[0 for i in range (100)]
    data_refund=[0 for i in range (100)]
    data_kritiksaran=[0 for i in range (100)]
    data_tiket_hilang=[0 for i in range (100)]
    
    print("Masukkan nama File User: ",end='')
    file_user = input()              # Global digunakan untuk mengkonversi variabel lokal menjadi variabel global sama seperti pada notasi algoritmik sebagai variabel yang dioutput                                           # Pada python tidak seperti notasi algoritmik variabel lokal yang diglobalkan tidak bisa dideklarasi sebagai parameter prosedur.
    input_data(file_user,data_user)
    print("Masukkan nama File Daftar Wahana: ",end='')
    file_wahana = input()

    input_data(file_wahana,data_wahana)
    print("Masukkan nama File Pembelian Tiket: ",end='')
    file_pembelian = input()
    
    input_data(file_pembelian, data_pembelian)
    print("Masukkan nama File Penggunaan Tiket: ",end='')
    file_penggunaan = input()
    
    input_data(file_penggunaan,data_penggunaan)
    print("Masukkan nama File Kepemilikan Tiket: ",end='')
    file_tiket = input()
    
    input_data(file_tiket,data_tiket)
    print("Masukkan nama File Refund Tiket: ",end='')
    file_refund = input()
    
    input_data(file_refund,data_refund)
    print("Masukkan nama File Kritik dan Saran: ",end='')
    file_kritiksaran = input()
    
    input_data(file_kritiksaran,data_kritiksaran)

    print("Masukkan nama File Tiket Hilang: ",end='')
    file_tiket_hilang = input()
    
    input_data(file_tiket_hilang,data_tiket_hilang)
    print()

    print("File perusahaan Willy Wangky’s Chocolate Factory telah di-load.")
    

def input_data(name_file,data_file):
    # fungsi mereturn data csv sebagai array
    with open(name_file) as filecsv:
        bacaCSV = csv.reader(filecsv)
        i=0
        for row in bacaCSV:
            data_file[i]=row
            i=i+1
    return

def nrows(data_file):
    i=0
    while ( data_file[i]!=0):
        i=i+1
    return i
#--------------------------------F02----------------------------------------------#
def save ():
    
    file = [
        input('Masukkan nama File User: '),
        input('Masukkan nama File Daftar Wahana: '),
        input('Masukkan nama File Pembelian Tiket: '),
        input('Masukkan nama File Penggunaan Tiket: '),
        input('Masukkan nama File Kepemilikan Tiket: '),
        input('Masukkan nama File Refund Tiket: '),
        input('Masukkan nama File Kritik Dan Saran: '),
        input('Masukkan nama File Tiket Hilang: ')
    ]
    print()
    print("Data berhasil disimpan!")
    output_data(file[0],data_user)
    output_data(file[1],data_wahana)
    output_data(file[2],data_pembelian)
    output_data(file[3],data_penggunaan)
    output_data(file[4],data_tiket)
    output_data(file[5],data_refund)
    output_data(file[6],data_kritiksaran)
    output_data(file[7],data_tiket_hilang)

def output_data(file_name,data_file):
    arsip= open(file_name, 'w', newline='')
    data=csv.writer(arsip,delimiter=',')
    for i in range(nrows(data_file)):
        data.writerow(data_file[i])
    arsip.close()
#--------------------------------F03----------------------------------------------#
def signup(data_user):
    print("Masukkan nama pemain: ",end='')
    namabaru = str(input())
    print("Masukkan tanggal lahir pemain (DD/MM/YYYY): ",end='')
    borndatebaru = str(input())
    print("Masukkan tinggi badan pemain (cm): ",end='')
    heightbaru = str(input())
    print("Masukkan username pemain: ",end='')
    usernamebaru = str(input())
    print("Masukkan password pemain: ",end='')
    passwordbaru = str(input())
    encryptedpasswordbaru = encrypt_password(passwordbaru)
    saldobaru = 0
    print() # Jadi, input dulu semua data yang diperlukan
    new_content=[namabaru,borndatebaru,heightbaru,usernamebaru,encryptedpasswordbaru,"Pemain",saldobaru]
                            
    if isFound(data_user,usernamebaru,3):
        print("Username tidak tersedia, Silahkan coba dengan username yang lain.")
    else:
        tambah_user(new_content)
        print("Selamat menjadi pemain, "+namabaru+". Selamat bermain.")
    return

def tambah_user(new_content):
    data_user[nrows(data_user)]=new_content # Baru nanti ditambah ke data_user pake fungsi append
    
    return
#--------------------------------F04----------------------------------------------#    
def login(username,password) :
    global login_status
    global role
    if (isFound(data_user,username,3)):
        i=idxFound(data_user,username,3)
        if (check_password(password, data_user[i][4])):
            print()
            print("Selamat bersenang-senang, " + data_user[i][0])
            role=data_user[i][5]
            login_status=True

        else:
            login_status=False
            print("Ups, password salah atau kamu tidak terdaftar dalam sistem kami. Silahkan coba lagi!")
    else:
        login_status=False
        print("Ups, password salah atau kamu tidak terdaftar dalam sistem kami. Silahkan coba lagi!")
    return

def idxFound(data_file,name,letak_label):
    # idxFound merupakan fungsi yang mengembalikan nilai indeks ditemukannya data
    # Kamus Lokal
    # i : integer
    # Algoritma Fungsi
    for i in range(nrows(data_file)):
        if (data_file[i][letak_label]== name):
            return int(i)

def isFound(data_file,name,letak_label):
    # isFound merupakan fungsi untuk menentukan username tersedia atau tidak
    # Kamus Lokal
    # i : integer
    # found = boolean
    found=False
    for i in range(nrows(data_file)):
        if (data_file[i][letak_label]== name):
            found=True
    return found

#--------------------------------F05----------------------------------------------#
def cari_pemain(username,data_user):
    # cari_pemain merupakan prosedur yang digunakan untuk mencari data pemain berdasarkan username
    # input : username
    # inisial state : username terdifinisi
    # final state : jika username ditemukan akan menampilkan data user ke layar, jika tidak menampilakn "Pemain tidak ditemukan

    # Algoritma Prosedur
    if isFound(data_user,username,3):
        indeks_data=idxFound(data_user,username,3)
        print("Nama Pemain: ",data_user[indeks_data][0])
        print("Tinggi Pemain: ",data_user[indeks_data][2])
        print("Tanggal Lahir Pemain: ",data_user[indeks_data][1])
    else : # jika username tidak ditemukan
        print("Pemain tidak ditemukan")

#--------------------------------F06----------------------------------------------#
def cari():
    
    print('''Jenis batasan umur:
1. Anak-anak (<17 tahun)
2. Dewasa (>=17 tahun)
3. Semua umur

Jenis batasan tinggi badan:
1. Lebih dari 170 cm
2.Tanpa batasan
''')

    batas_umur = input("Batasan umur pemain: ")
    while (batas_umur != "1" ) and (batas_umur != "2" ) and (batas_umur != "3" ):
        print("Batasan umur tidak valid!")
        batas_umur = input("Batasan umur pemain: ")
    batas_tinggi = input("Batasan tinggi badan: ")
    while (batas_umur != "1" ) and (batas_umur != "2" ) :
        print("Batasan tinggi badan tidak valid!")
        batas_tinggi = input("Batasan tinggi badan: ")

    print('\nHasil pencarian:')

    found = False
    for i in range(nrows(data_wahana)):
        if (data_wahana[i][3] == batas_umur) and (data_wahana[i][4] == batas_tinggi) :
            print(f'{data_wahana[i][0]} | {data_wahana[i][1]} | {data_wahana[i][2]}')
            found = True
    if not found:
        print('Tidak ada wahana yang sesuai dengan pencarian kamu.')


#--------------------------------F07----------------------------------------------#
def beli_tiket():
    n = 0 # n adalah indeks user
    indeksuserketemu = False
    while (not indeksuserketemu):
        if(data_user[n][3] == username):
            indeksuserketemu = True
        else:
            n = n + 1
    print("Masukkan ID wahana: ",end='')
    idwahana = str(input())
    print("Masukkan tanggal hari ini: ",end='')
    todate = str(input())
    print("Jumlah tiket yang dibeli: ",end='')
    jumlahtiket = int(input())
    print()
    isFound = False
    i = 0
    while((not isFound)): # Cari dulu indeks wahana yang diinput user
        if(data_wahana[i][0] == idwahana):
            isFound = True # Indeks wahana ditemukan
        else:
            i = i + 1
    tanggallahir = data_user[n][1] # Ambil data tanggal lahir user
    tinggiuser = int(data_user[n][2])
    batastinggi = nilaibatastinggi(data_wahana[i][4])
    batasumur = nilaibatasumur(data_wahana[i][3])
    if(tinggiuser >= batastinggi) and (cekumur(tanggallahir,todate,batasumur)): # Cek batas tinggi dan batas umur
        saldouser = int(data_user[n][6])
        harga1tiket = int(data_wahana[i][2])
        saldotergunakan = harga1tiket * jumlahtiket
        if(saldouser >= saldotergunakan):
            print("Selamat bersenang-senang di "+data_wahana[i][1]+".")
            data_user[n][6] = saldouser - saldotergunakan
            new_tiket_content = [data_user[n][3],data_wahana[i][0],str(jumlahtiket)]
            tambah_tiket(new_tiket_content)
            new_pembelian_content = [data_user[n][3],todate,data_wahana[i][0],str(jumlahtiket)]
            tambah_pembelian(new_pembelian_content)
        else:
            print("Saldo Anda tidak cukup.")
            print("Silakan mengisi saldo Anda.")
    else:
        print("Anda tidak memenuhi persyaratan untuk memainkan wahana ini.")
        print("Silakan menggunakan wahana lain yang tersedia.")

def nilaibatastinggi(batastinggi):
    if (batastinggi == "1"):
        return 170
    elif (batastinggi == "2"):
        return 0

def nilaibatasumur(batasumur):
    if (batasumur == "1"):
        return (-17) # Untuk kasus kurang dari 17 tahun
    elif (batasumur == "2"):
        return 17
    elif (batasumur == "3"):
        return 0

def tambah_tiket(new_tiket_content):
    data_tiket[nrows(data_tiket)]=new_tiket_content

def tambah_pembelian(new_pembelian_content):
    data_pembelian[nrows(data_pembelian)]=new_pembelian_content

def cekumur(tanggallahir,todate,batasumur):
    if (batasumur == 17):
        bornyear = str(tanggallahir[6])+str(tanggallahir[7])+str(tanggallahir[8])+str(tanggallahir[9]) # Tahun lahir dalam string
        bornyearint = int(bornyear) # Konversi ke integer
        yearnow = str(todate[6])+str(todate[7])+str(todate[8])+str(todate[9]) # Tahun ini dalam string
        yearnowint = int(yearnow) # Konversi ke integer
        bornmonth = str(tanggallahir[3])+str(tanggallahir[4])
        bornmonthint = int(bornmonth)
        monthnow = str(todate[3])+str(todate[4])
        monthnowint = int(monthnow)
        bornday = str(tanggallahir[0])+str(tanggallahir[1])
        borndayint = int(bornday)
        daynow = str(todate[0])+str(todate[1])
        daynowint = int(daynow)
        if(yearnowint - bornyearint > batasumur): # Kasus saat selisih tahun sekarang dan tahun lahir lebih dari batas umur
            return True # Dengan kata lain, pengguna sudah cukup umur untuk menggunakan wahana
        elif(yearnowint - bornyearint < batasumur): # Kasus saat selisih tahun sekarang dan tahun lahir kurang dari batas umur
            return False # Dengan kata lain, pengguna belum cukup umur
        else: # Kasus khusus saat selisihnya adalah batas umur, perlu pemeriksaan lebih lanjut (bulan dan hari lahir)
            if(monthnowint > bornmonthint): # Jika bulan sekarang sudah lebih dari bulan lahir, artinya umurnya sudah bertambah
                return True # Sehingga cukup umur
            elif(monthnowint < bornmonthint): # Jika belum, artinya umurnya belum cukup
                return False
            else: # Jika bulan sekarang adalah bulan lahirnya, cek hari
                if(daynowint >= borndayint): # Jika hari ini lebih dari atau sama dengan hari lahirnya, artinya umurnya sudah bertambah
                    return True
                else:
                    return False
    elif (batasumur == (-17)):
        batasumur = 17 # Ubah batas umur ke 17, tetapi kita akan meninjau untuk kasus yang sebaliknya
        bornyear = str(tanggallahir[6])+str(tanggallahir[7])+str(tanggallahir[8])+str(tanggallahir[9]) # Tahun lahir dalam string
        bornyearint = int(bornyear) # Konversi ke integer
        yearnow = str(todate[6])+str(todate[7])+str(todate[8])+str(todate[9]) # Tahun ini dalam string
        yearnowint = int(yearnow) # Konversi ke integer
        bornmonth = str(tanggallahir[3])+str(tanggallahir[4])
        bornmonthint = int(bornmonth)
        monthnow = str(todate[3])+str(todate[4])
        monthnowint = int(monthnow)
        bornday = str(tanggallahir[0])+str(tanggallahir[1])
        borndayint = int(bornday)
        daynow = str(todate[0])+str(todate[1])
        daynowint = int(daynow)
        if(yearnowint - bornyearint < batasumur): # Kasus saat selisih tahun sekarang dan tahun lahir kurang dari batas maksimal umur
            return True # Dengan kata lain, pengguna cukup muda untuk menggunakan wahana
        elif(yearnowint - bornyearint > batasumur): # Kasus saat selisih tahun sekarang dan tahun lahir lebih dari batas maksimal umur
            return False # Dengan kata lain, pengguna terlalu tua
        else: # Kasus khusus saat selisihnya adalah batas maksimal umur, perlu pemeriksaan lebih lanjut (bulan dan hari lahir)
            if(monthnowint < bornmonthint): # Jika bulan sekarang masih kurang dari bulan lahir, artinya umurnya belum di batas maksimal
                return True # Sehingga cukup umur
            elif(monthnowint > bornmonthint): # Jika sudah, artinya pengguna sudah melewati batas maksimal umur
                return False
            else: # Jika bulan sekarang adalah bulan lahirnya, cek hari
                if(daynowint < borndayint): # Jika hari lahirnya belum lewat, maka pengguna masih cukup muda
                    return True
                else:
                    return False
    elif (batasumur == 0):
        return True
#--------------------------------F08----------------------------------------------#
def gunakantiket(username,data_wahana,data_tiket) :
    id_wahana = str(input("Masukkan ID wahana: "))
    tanggal = str(input("Masukkan tanggal hari ini: "))
    jumlah_ticket = str(input("Jumlah tiket yang digunakan: "))
    terdapat_wahana = False
    terdapat_tiket = False
    terdapat_username = False
    for i in range (nrows(data_wahana)) :
        if data_wahana[i][0] == id_wahana :
            terdapat_wahana = True
            break
    if terdapat_wahana == False :
        print("Tiket Anda tidak valid dalam sistem kami")
    if terdapat_wahana == True :
        for j in range (nrows(data_tiket)) :
            if data_tiket[j][0] == username and data_tiket[j][1] == id_wahana :
                terdapat_username = True
                break
        if terdapat_username == False :
            print("Tiket Anda tidak valid dalam sistem kami")
        elif terdapat_username == True :
            if int(data_tiket[j][2]) >= int(jumlah_ticket) :
                print("Terima kasih telah bermain")
                data_penggunaan[nrows(data_penggunaan)]= [username, tanggal, id_wahana, jumlah_ticket]
                data_tiket[j][2]=str(int(data_tiket[j][2])-int(jumlah_ticket))
            else :
                print("Tiket Anda tidak cukup")
    return

#--------------------------------F09----------------------------------------------#
def is_refund_valid(username,ID_Wahana,Jumlah_Tiket,data_tiket):
    # is_refund_valid merupakan fungsi yang digunakan untuk mengecheck apakah pemain memeiliki tiket yang direfund
    # is_refund_valid akan mereturn nilai boolean, jika terdapat tiket akan mereturn True jika tidak False
    
    valid= False
    for i in range (nrows(data_tiket)): # Digunakan untuk mengecheck semua array di data_tiket 
        if (data_tiket[i][0] == username) and (data_tiket[i][1] == ID_Wahana) and (int(data_tiket[i][2]) >= int(Jumlah_Tiket)):
            # digunakan untuk mengecheck username dan jumlah tiket pada indeks yang sama
            valid=True
    return valid

def refund(username,data_tiket,data_refund,data_user):
    ID_Wahana= input("Masukkan ID wahana: ")
    Tanggal_Refund=input("Masukkan Tanggal Refund: ")
    Jumlah_Tiket= int(input("Jumlah tiket yang di-refund: "))
    if is_refund_valid(username,ID_Wahana,Jumlah_Tiket,data_tiket):
        for i in range(nrows(data_tiket)):
            if (data_tiket[i][0] == username) and (data_tiket[i][1] == ID_Wahana):
                # digunakan untuk memperoleh indeks username yang akan direfund
                indeks=i
        data_tiket[indeks][2]=str(int(data_tiket[indeks][2])- Jumlah_Tiket)
        # jumlah tiket pemain akan dikurangi
        data_refund[nrows(data_refund)]=[username,Tanggal_Refund,ID_Wahana,Jumlah_Tiket]
        # data refund akan ditambahkan ke array
        idxwahana=idxFound(data_wahana,ID_Wahana,0)
        # digunakan untuk mencari indeks wahana
        harga_tiket = int(data_wahana[idxwahana][2])
        # digunakan untuk mngetahui harga tiket
        idxuser=idxFound(data_user,username,3)
        data_user[idxuser][6]=str(int(data_user[idxuser][6])+0.8*harga_tiket*Jumlah_Tiket)
        # saldo user akan ditambahkan sebesar 80 persen harga tiket yang direfund
        print()
        print("Uang refund sudah kami berikan pada akun Anda.")
        
    else :
        print("Kamu tidak memiliki tiket tersebut")
    return


#--------------------------------F10----------------------------------------------#
def kritik_saran(username,data_kritiksaran):
    id_wahana = input('Masukkan ID Wahana: ')
    tanggal = input('Masukkan tanggal pelaporan: ')
    kritik = input('Kritik/saran Anda: ')

    data_kritiksaran[nrows(data_kritiksaran)]=[username, tanggal, id_wahana, kritik]
    
    print()
    print("Kritik dan saran Anda kami terima.")
    return

#--------------------------------F11----------------------------------------------#
def lihat_laporan(data_kritiksaran):
    print("Kritik dan saran:")
    N = nrows(data_kritiksaran)
    if (N > 1): # Digunakan skema selection sort (dengan sedikit perubahan) untuk mengurutkan data_kritiksaran sesuai alphabet
        for Pass in range(N-1):
            IMax = Pass
            for i in range(Pass+1,N):
                if(data_kritiksaran[IMax][2] >= data_kritiksaran[i][2]):
                    IMax = i
            Temp = data_kritiksaran[IMax]
            data_kritiksaran[IMax] = data_kritiksaran[Pass]
            data_kritiksaran[Pass] = Temp
    for i in range(nrows(data_kritiksaran)): # Setelah diurutkan, data_kritiksaran ditampilkan ke layar
        print(data_kritiksaran[i][2]+" | "+data_kritiksaran[i][1]+" | "+data_kritiksaran[i][0]+" | "+data_kritiksaran[i][3])

#--------------------------------F12----------------------------------------------#
def tambah_wahana(data_wahana) :
    print("Masukkan Informasi Wahana yang ditambahkan: ")
    id_wahana_tambahan = str(input("Masukkan ID Wahana: "))
    nama_wahana = str(input("Masukkan Nama Wahana: "))
    harga_tiket_wahana = str(input("Masukkan Harga Tiket: "))
    batasan_umur = str(input("Batasan Umur: "))
    while (batasan_umur != "anak-anak") and (batasan_umur != "dewasa") and (batasan_umur != "semua umur") : 
        print("Masukkan batasan umur yang valid (anak-anak, dewasa, atau semua umur)")
        batasan_umur = str(input("Batasan Umur: "))
    if batasan_umur == "anak-anak" :
        batasan_umur = "1"
    elif batasan_umur == "dewasa" :
        batasan_umur = "2"
    elif batasan_umur == "semua umur" :
        batasan_umur = "3" 
    batasan_tinggi_badan = str(input("Batasan tinggi badan: "))
    while (batasan_tinggi_badan != "Tanpa batasan") and (batasan_tinggi_badan != "Lebih dari 170 cm") :
        print("Masukkan batasan tinggi badan yang valid (Tanpa batasan atau Lebih dari 170 cm)")
        batasan_tinggi_badan = str(input("Batasan tinggi badan: "))
    if batasan_tinggi_badan == "Lebih dari 170 cm" :
        batasan_tinggi_badan = "1"
    elif batasan_tinggi_badan == "Tanpa batasan" :
        batasan_tinggi_badan = "2"
    data_wahana[nrows(data_wahana)]=[id_wahana_tambahan, nama_wahana, harga_tiket_wahana, batasan_umur, batasan_tinggi_badan]
    return

#--------------------------------F13----------------------------------------------#
def topup(data_user):
    username=input("Masukkan username: ")
    saldo=int(input("Masukkan saldo yang di-top up: "))
    
    if isFound(data_user,username,3):
        # untuk mengecheck username yang akan di-topup
        indeks_data = idxFound(data_user,username,3)
        # digunakan untuk mencari indeks username
        data_user[indeks_data][6]=str(int(data_user[indeks_data][6])+saldo)
        # digunakan untuk menambahkan saldo
        print()
        print("Top up berhasil. Saldo "+data_user[indeks_data][0]+" bertambah menjadi "+str(data_user[indeks_data][6]))
    else:
        print("username tidak ditemukan")
        
#--------------------------------F14----------------------------------------------#
def riwayat_pengguna(data_penggunaan):
    id_wahana = input('Masikkan ID Wahana: ')

    print('Riwayat:')

    found = False
    for i in range(nrows(data_penggunaan)):
        if data_penggunaan[i][2] == id_wahana:
            print(f'{data_penggunaan[i][1]} | {data_penggunaan[i][0]} | {data_penggunaan[i][3]}')
            found = True
    if not found:
        print('Tidak ada riwayat penggunaan')

#--------------------------------F15----------------------------------------------#
def tiket_pemain(data_tiket,data_wahana):
    print("Masukkan username: ",end='')
    username = str(input())
    print("Riwayat:")
    for i in range(nrows(data_tiket)):
        if(data_tiket[i][0] == username):
            print(data_tiket[i][1]+" | "+str(carinama(data_tiket[i][1]))+" | "+str(data_tiket[i][2]))

def carinama(wahana):
    for i in range(nrows(data_wahana)):
        if (data_wahana[i][0] == wahana):
            return data_wahana[i][1]
   
#--------------------------------F16----------------------------------------------#
def exit():
    global login_status
    save_status = input("Apakah anda mau melakukan penyimpanan file yang sudah dilakukan (Y/N)? ")
    login_status = False
    if (save_status == "Y"):
        save()
    return

#--------------------------------B01----------------------------------------------#
# Import modul penting
import base64
import hashlib
import hmac
import secrets

def encrypt_password(passwd):
    # Mengenkripsi password menggunakan pbkdf2_hmac
    # Input:
    #  passwd : string { input password }
    # Output : string { password yang sudah dienkripsi }
    # KAMUS LOKAL
    #  hash_name : string { nama hash }
    #  n : integer { jumlah iterasi }
    #  salt : string
    #  hash : string

    # Parameter hash
    hash_name = 'sha256'
    n = 100000
    salt = secrets.token_bytes(64)

    # Konversi password ke bytes (karena fungsi hash meminta itu)
    # (jangan terlalu dipikirkan)
    passwd = bytes(passwd, 'utf-8')

    hash = hashlib.pbkdf2_hmac(hash_name, passwd, salt, n)

    # Enkoding ke base-64
    return str(base64.urlsafe_b64encode(salt+hash), 'utf-8')

def check_password(passwd, saved_passwd):
    # Mengecek password apakah sama
    # Input:
    #  passwd : string { input password }
    #  saved_passwd : string { password yang disimpan }
    # Output : bool { true jika sama }

    # KAMUS LOKAL
    #  hash_name : string { nama hash }
    #  n : integer { jumlah iterasi }
    #  salt : string
    #  hash : string
    #  saved_hash : string

    # Dekoding dari base-64
    saved_passwd = base64.urlsafe_b64decode(bytes(saved_passwd, 'utf-8'))

    # Parameter hash
    hash_name = 'sha256'
    n = 100000
    salt = saved_passwd[:64]

    # Konversi password ke bytes (karena fungsi hash meminta itu)
    # (jangan terlalu dipikirkan)
    passwd = bytes(passwd, 'utf-8')

    hash = hashlib.pbkdf2_hmac(hash_name, passwd, salt, n)

    saved_hash = saved_passwd[64:]

    # Menggunakan fungsi hmac.compare_digest untuk keamanan
    return hmac.compare_digest(hash, saved_hash)

#--------------------------------B03----------------------------------------------#
def best_wahana(): # Idenya adalah meninjau data pembelian
    arrwahana = [0 for i in range(100)]
    for i in range(nrows(data_wahana)):
        idwahana = data_wahana[i][0]
        namawahana = data_wahana[i][1]
        tiketwahanaterbeli = 0
        new_content = [idwahana,namawahana,tiketwahanaterbeli]
        arrwahana[nrows(arrwahana)] = new_content # Jadi arrwahana ini data yang akan ditulis ke layar
    idwahanapembelian = [0 for i in range(nrows(data_pembelian))]
    for i in range(nrows(data_pembelian)):
        idwahanapembelian[i] = data_pembelian[i][2]
    idwahanaarrwahana = [0 for i in range(nrows(data_wahana))]
    for i in range(nrows(arrwahana)):
        idwahanaarrwahana[i] = arrwahana[i][0]
    for i in range(nrows(arrwahana)): # Hitung dulu jumlah tiket wahana yang terbelinya
        for j in range(nrows(data_pembelian)):
            if (idwahanapembelian[j] == idwahanaarrwahana[i]): # Tinjau data pembelian, kalo ini sama (True), artinya arrwahana[j][0] ada yang beli
                arrwahana[i][2] = int(arrwahana[i][2]) + int(data_pembelian[i][3])
    if (nrows(arrwahana) > 1):
        for Pass in range(1,nrows(arrwahana)):
            Temp = int(arrwahana[Pass][2])
            tempgeser = arrwahana[Pass]
            i = Pass - 1
            while (Temp >= int(arrwahana[i][2]) and i > 0):
                arrwahana[i+1] = arrwahana[i]
                i = i - 1
            if (Temp <= int(arrwahana[i][2]) or i == 1):
                arrwahana[i+1] = tempgeser
            else:
                arrwahana[i+1] = arrwahana[i]
                arrwahana[i] = tempgeser
    for i in range(3):
        print(str(i+1)+" | "+arrwahana[i][0]+" | "+arrwahana[i][1]+" | "+str(arrwahana[i][2]))
    return
#--------------------------------B04----------------------------------------------#
def tiket_hilang ():
    username = input("Masukkan username: ")
    tanggal= input("Tanggal kehilangan tiket: ")
    Id_wahana = input("ID wahana: ")
    jumlah_tiket = int(input("Jumlah tiket yang dihilangkan: "))
    data_tiket_hilang[nrows(data_tiket_hilang)]=[username,tanggal,Id_wahana,jumlah_tiket]
    print()
    print("Laporan kehilangan tiket Anda telah direkam.")
    if idxFound(data_tiket,username,0)== idxFound(data_tiket,Id_wahana,1):
        indeks_data=idxFound(data_tiket,username,0)
        data_tiket[indeks_data][2]=str(int(data_tiket[indeks_data][2])-jumlah_tiket)
    
    return

#--------------------------------Program UTAMA----------------------------------------------#
login_status=False
load_status=False
program=True

while (program):
    perintah = input("$ ")
    if (perintah=="load"):
        load()
        load_status=True
    else:
        if (load_status==True):
            if (perintah=="save"):
                save()
                
            elif(perintah=="login"):
                if(login_status==True):
                    print("Kamu sudah login. Silahkan keluar terlebih dahulu.")
                else:
                    username = str(input("Masukkan username: "))
                    password = str(input("Masukkan password: "))
                    login(username,password)
            elif(perintah=="save"):
                save()
            elif (perintah=="exit"):
                exit()
            else:
                if(login_status==True):
                    if(perintah=="signup"):
                        if (role=="Admin"):
                            signup(data_user)  
                        else:
                            print("Maaf, hanya admin yang dapat menggunakan fitur ini")
                            
                    elif(perintah=="cari_pemain"):
                        if (role=="Admin"):
                            name=input("Masukkan username: ")
                            cari_pemain(name,data_user)
                            
                        else:
                            print("Maaf, hanya admin yang dapat menggunakan fitur ini")
                            
                    elif(perintah=="main"):
                        if (role=="Pemain"):
                            gunakantiket(username,data_wahana,data_tiket)
                        else:
                            print("Maaf, hanya pemain yang dapat menggunakan fitur ini")
                            
                    elif(perintah=="refund"):
                        if (role=="Pemain"):
                            refund(username,data_tiket,data_refund,data_user)
                        else:
                            print("Maaf, hanya pemain yang dapat menggunakan fitur ini")
                            

                    elif(perintah=="kritik_saran"):
                        if (role=="Pemain"):
                            kritik_saran(username,data_kritiksaran)
                        else:
                            print("Maaf, hanya pemain yang dapat menggunakan fitur ini")
                           
                    elif(perintah=="lihat_laporan"):
                        if (role=="Admin"):
                            lihat_laporan(data_kritiksaran)
                        else:
                            print("Maaf, hanya admin yang dapat menggunakan fitur ini")

                        

                    elif(perintah=="tambah_wahana"):
                        if (role=="Admin"):
                            tambah_wahana(data_wahana)
                        else:
                            print("Maaf, hanya admin yang dapat menggunakan fitur ini")

                    elif(perintah=="topup"):
                        if (role=="Admin"):
                            topup(data_user)
                        else:
                            print("Maaf, hanya admin yang dapat menggunakan fitur ini")

                    elif(perintah=="riwayat_wahana"):
                        if (role=="Admin"):
                            riwayat_pengguna(data_penggunaan)
                        else:
                            print("Maaf, hanya admin yang dapat menggunakan fitur ini")

                    elif(perintah=="tiket_pemain"):
                        if (role=="Admin"):
                            tiket_pemain(data_tiket,data_wahana)
                        else:
                            print("Maaf, hanya admin yang dapat menggunakan fitur ini")
                            
                    elif(perintah=="cari"):
                        cari()

                    elif(perintah=="best_wahana"):
                        best_wahana()
                        
                    elif(perintah=="beli_tiket"):
                        beli_tiket()

                    elif(perintah=="tiket_hilang"):
                        tiket_hilang()

                else:
                    print("Kamu belum login. Silahkan login terlebih dahulu")
                    
        else:
            print("Kamu harus load terlebih dahulu")
