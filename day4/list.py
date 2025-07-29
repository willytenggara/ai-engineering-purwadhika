# Access Data Range of Indexes
listContoh = ['hello', 1, 1, 3, True]
# print(listContoh[-4:-1]) # this is range, slicing the list using negative indexes. 
# print(listContoh[2:]) # ini juga range, dapatkan semua item dari index ke 2 sampai akhir
print(listContoh[1:3]) # start dari index 1, dan berakhir SEBELUM index 3
print(listContoh[:]) # ini untuk mengambil semua isi di dalam list
# print(len(listContoh))

# Mengakses list di dalam list // 2D list
angka = [1,2,3,[4,5,6]] # list 2 dimensi
# cara 1
# print(angka[3][0])
# cara 2
angka_dalam = angka[3]
# print(angka_dalam[0])

new_list = [1,[2,3,[4,5,6]]]
# print(new_list[1][2][2])