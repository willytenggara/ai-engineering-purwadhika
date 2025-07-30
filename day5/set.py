# Set dibutuhkan untuk mengetahui data yang unik, men-solve problem terkait duplikasi data

#? Syntax set
from tabnanny import check


setContoh = {'The Avengers', 'Iron Man 3', 'Captain America: Civil War', 'Iron Man 3'}
# print(setContoh) # {'Captain America: Civil War', 'Iron Man 3', 'The Avengers'}
#? The order of the items will always be random

#* Create Set from List, Tuple, and Dictionary
list1 = ['Budi', 2, 2, 'Ceci']
tuple1 = (False, 1, 'Andi', False)
dictionary1 ={
  'nama': "Coder",
  'usia':25,
  'pekerjaan':'Coder',
  'menikah': False
}
setList = set(list1)
setTuple = set(tuple1)
setDictionary = set(dictionary1)
setDictionaryValue= set(dictionary1.values())

# print(setList)
# print(setTuple)
# print(setDictionary)
# print(setDictionaryValue)

#* Access Data
# for item in setContoh:
#   print(item)

#* Check if an Item exist in a Set
# if 'Iron Man 3' in setContoh:
#   print('Ada Iron Man 3')
# else:
#   print('Tidak ada Iron Man 3')

#* Add Data
setContoh.add('Thor') #? Method add hanya menambahkan 1 item saja
# print(setContoh)
setContoh.update({'Captain America', 'Hulk'}) #? Method update menambahkan beberapa item sekaligus
# print(setContoh)

#* Delete Data
setContoh.remove('Thor') 
# print(setContoh)
setContoh.discard('Captain America')
# print(setContoh)
setContoh.pop()
# print(setContoh)
setContoh.clear()
# print(setContoh)

#* Length of Set
# print(len(setContoh))


#* Join Sets
setMovie1 = {'The Avengers', 'Iron Man 3', 'Avengers: Age of Ultron', 'Hulk'}
setMovie2 = {'Titanic', 'The Avengers', 'Hulk'}

setGabungan = setMovie1.union(setMovie2)
# print(setGabungan)


#* Get DIFFERENCE between 2 sets -> Mengambil apa yang di kiri, dan menghilangkan apa yang sama antara set di kiri (movie1) dan kanan (movie2)
# setMovie3 = setMovie1.difference(setMovie2) #? Create a new set setMovie3 containing all items that are in setMovie1 but not in setMovie2.
#! it finds the difference between the two sets—removing any items from setMovie1 that also exist in setMovie2.
# print(setMovie3) #? The result is a set of unique items only found in setMovie1.
# print(setMovie1)
#* Cara atas dan bawah sama saja tujuannya
# setMovie1.difference_update(setMovie2) #? Removes the items in this set that are also included in another, specified set
# print(setMovie1)


#* Get SYMMETRIC DIFFERENCE between 2 sets -> returns a new set containing all items that are in either of the two sets, BUT not in both.
setMovie3 = setMovie1.symmetric_difference(setMovie2) #? in other words, it gives you the elements that are unique to each set (not shared).
# print(setMovie3)
# print(setMovie1)
#! Cara atas dan bawah sama saja tujuannya
# setMovie1.symmetric_difference_update(setMovie2) #? Menghilangkan apa yang sama antara set1 dan set2
# print(setMovie1)


#* Get INTERSECTION between 2 sets -> mengambil HANYA item yang sama diantara kedua set
setMovie3 = setMovie1.intersection(setMovie2)
# print(setMovie3)
# print(setMovie1)
#! Cara atas dan bawah sama saja tujuannya
# setMovie1.intersection_update(setMovie2)
# print(setMovie1)


#* Check DISJOINT, SUBSET, and SUPERSET -> return boolean
#? DISJOINT -> Two sets are disjoint (TRUE) if they HAVE NO ELEMENTS IN COMMON.
checkDisjoint = setMovie1.isdisjoint(setMovie2)
# print(checkDisjoint)

setMovieFirst= {'Titanic'}
setMovieSecond = {'Avenger'}
checkDisjoint2 = setMovieFirst.isdisjoint(setMovieSecond)
# print(checkDisjoint2)


#? SUBSET -> A set is a subset of another set if ALL ELEMENTS of the FIRST set are also in the SECOND (Parameter) set
# Returns True if every element of set1 is in set2.
setMovieFirst2 = {'Titanic'}
setMovieSecond2 = {'Titanic', 'Sore'}
# print(setMovieSecond2.issubset(setMovieFirst2)) # FALSE

checkSubset = setMovieFirst2.issubset(setMovieSecond2)
# print(checkSubset) # TRUE


#? SUPERSET -> A set is a superset of another set if ALL ELEMENTS of the SECOND (Parameter) set are also in the FIRST set.
checkSuperset = setMovieFirst2.issuperset(setMovieSecond2)
print(checkSuperset) # FALSE

print(setMovieSecond2.issuperset(setMovieFirst2)) # TRUE



