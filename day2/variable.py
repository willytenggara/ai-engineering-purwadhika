import math
# print("Hellow World")
pesan = "Selamat Datang di Python"
pesan = "Selamat Jalan"
# print(pesan)

# Tipe data list
buah = ['jeruk','mangga'] 

# Tipe data tuple
buah2 = ("jeruk", "mangga", "apel")

# Tipe data dictionary
x = {"nama":"Will", "umur":31}
y = None
z = range(2)


# print(buah[1])
# print(x["nama"])
# print(z)
# print(10.5%4) # remainder after divisions
# print(2**2)
# print(11//2)

a = 10
a+=2
# print(a)

# Pembagian floor //, akan dibulatkan nilainya ke bawah. 
# print(math.pow(2,3))
# print(math.floor(2.9))
# print(math.ceil(2.01))

kutipSatu = 'Kutip Satu("I am Will")'
kutipDua = "I'm Batman"
kutipTiga = '''
I'm Batman:
"I'm Ironman"
 '''
escapeCharacter = "Salam kenal murid \"Purwadhika\", mari kita belajar bersama"

# print(kutipSatu)
# print(kutipDua)
# print(kutipTiga)
# print(escapeCharacter)


# Method Len
kata = "Batman\tGundam"
kalimat = "Saya adalah Batman"
# print(kata)
# print(len(kalimat))

umur = 23
kalimat = "Nama saya Willy, umur saya {}."
kalimatLengkap = kalimat.format(umur)
kalimat_lengkap = f"Nama saya adalah Willy, umur saya {umur} tahun."
print(kalimat_lengkap)

nama = input("Masukkan nama: ")
txt = "Tenggara" in nama
# print(txt)