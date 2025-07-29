stars = ''
size = 5
for i in range(size): # iterasi pertama i adalah 0
  print(f'index-i : {i}')
  for j in range(1 + i):
    print(f'\tindex-j : {j}')
    stars += '* '
  stars += '\n'
  print(stars)
  # 0, 1, 2, 3