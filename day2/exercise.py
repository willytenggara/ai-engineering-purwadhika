import math
#* Soal 1
x = 4
y = 3
z = 2

numerator = x+y*z
denominator = x*y

fraction = numerator/denominator
w = fraction ** z
# print(w)

#* Soal 2
# Silahkan masukkan angka berapapun : 5
# Kuadrat dari 5 = 25

angka = input("Silahkan masukkan angka berapapun: ")
kuadrat = int(angka) ** 2
# print(f"Kuadrat dari {angka} = {kuadrat}")

#* Soal 3
# 485 hari, nyatakan dalam tahun, bulan, minggu dan hari.
# 1 bulan =  30 hari, 1 tahun = 360 hari

hari = 485
bulan = 30
tahun = 360

tahun = hari%360

print(tahun)