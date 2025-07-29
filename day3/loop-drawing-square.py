stars = ''
size = 5
for i in range(size): # iterasi pertama i adalah 0
  # print(f'index-i : {i}')
  for j in range(size): # selama iterasi i masih 0, j harus jalan dullu dari 0 - 4
    # print(f'\tindex-j : {j}')
    stars += '* ' # terus gambar bintang
  stars += '\n' # setelah j sudah selesai, baru kasih enter terus balik ke atas dimulai i = 1 untuk iterasi ke 2
# print(stars)