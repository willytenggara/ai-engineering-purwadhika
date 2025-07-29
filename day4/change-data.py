pilihan = ['ya','tidak']
# print(pilihan)
pilihan[0]='mungkin'
# print(pilihan)

# Add Data (the last index of list)
pilihan.append('iya')
# print(pilihan)

# Insert (inserting data onto desired index)
pilihan.insert(2,'bisa jadi') # it has 2 parameters -> (index, value)
# print(pilihan)

# Remove (define what to remove specific value in the list)
pilihan.remove('bisa jadi')
# print(pilihan)  

# Pop (remove the last index of the list)
pilihan.pop()
# print(pilihan)

# Delete (delete specific item using index, similar to remove)
del pilihan[0] 
# print(pilihan)

# Clear (remove all items)
pilihan.clear()
# print(pilihan)

# Looping the list
keranjang_buah = ['apel','mangga','jeruk','anggur','manggis','semangka','durian']
# for nama_buah in keranjang_buah:
#     print(nama_buah)

# Check if an item exist in a list
# if 'mangga' in keranjang_buah:
#   print('buah tersedia')
# else:
#   print('buah tidak tersedia')

# Copy a list
keranjang_buah_2 = keranjang_buah.copy() # untuk kasus dimana kita tidak mau merusak variable yang sebelumnya
# print(keranjang_buah_2)

# Join 2 lists - List Concatenating
listContoh = ['hello', 1, 1, 3, True]
listBaru = [5, 'test']
listGabungan = listContoh + listBaru
# print(listGabungan) OR using .extend()
listContoh.extend(listBaru)
print(listContoh)

# Find Index
# print(keranjang_buah.index('mangga'))

# Sorting
listNama = ['eddie','baron','andi','charlie','samson']
listNama.sort()
print(listNama)
listNama.sort(reverse=True) # listNama.reverse()
print(listNama)


