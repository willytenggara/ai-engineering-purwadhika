# Create dictionary
# cara 1
dictionaryContoh1 = {
  "nama": "Will",
  "umur": 28,
  'pekerjaan': 'Developer'
}
# print(dictionaryContoh1)

# cara 2
dictionaryContoh2 = dict(nama = 'Willy', usia = 27, pekerjaan = 'AI Engineer')
# print(dictionaryContoh2)

#? Access Data
dictionaryContoh = {
  "nama": "Will",
  "umur": 28,
  'pekerjaan': 'Developer',
  'menikah': False
}

# print(dictionaryContoh['nama'])
# print(dictionaryContoh.get('menikah'))

#? Change Data
dictionaryContoh['nama'] = 'Bernard'
# print(dictionaryContoh)

#? Add Data
dictionaryContoh['kelamin'] = 'Laki-laki'
# print(dictionaryContoh)

#! Delete Data
# del dictionaryContoh['kelamin'] # removes key-value pair for kelamin key
# dictionaryContoh.pop('umur') # removes key-value pair for usia key
# dictionaryContoh.popitem() # removes last key-value pair
# print(dictionaryContoh)

# dictionaryContoh.clear() # empties the dictionary
# print(dictionaryContoh)

#? Loop through dictionary
# for k in dictionaryContoh: # k adalah nama variable
#   print("{}:{}".format(k, dictionaryContoh[k])) # k adalah nama variable
#! Kedua cara diatas dan dibawah sama, untuk loop key
# for key in dictionaryContoh.keys():
#   print("{}:{}".format(key, dictionaryContoh[key]))

# for val in dictionaryContoh.values():
#   print(val)

# print(dictionaryContoh.keys()) #? display all keys as view object
# print(dictionaryContoh.values()) #? display all values as a view object
# print(dictionaryContoh.items()) #? returns a view object that contains pairs of keys and values from the dictionary as tuples.

# for key,val in dictionaryContoh.items(): #? This code loops through all key-value pairs in the dictionary 
#   print("{}:{}".format(key, val)) #? For each pair, it prints the key and its value in the format key:value

#* Check if a key exist in a Dictionary
# if 'usia' in dictionaryContoh:
#   print('Ada key usia')
# else:
#   print('Tidak ada key usia')

#* Length of Dictionary
# print(len(dictionaryContoh))

#* Dictionary inside dictionary
menu ={
  'food1': {
    'name' : 'Ramen',
    'price' : 10000
  },
  'food2': {
    'name' : 'Pizza',
    'price' : 15000
  },
  'food3': {
    'name' : 'Sushi',
    'price' : 20000 
  }
}

# print(menu['food1']['name'])
# print(menu['food3'])

things = {
  "restaurant1": ["ramen","tea"],
  "restaurant":["pizza", "sphagetti"]
}

# print(things['restaurant'][0]) #? ini adalah cara mengakses data pada dictionary dan list yang ada didalam dictionary