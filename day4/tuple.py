# Perbedaan Tuple dan List adalah tuple itu TIDAK BISA di modifikasi datanya. 
# Semua method untuk mengakses tetap sama seperti list
# Kita butuh tuple karena kita kadang membutuhkan sebuah data yang tidak bisa diubah / fix

# Change Data - Tuple can be converted to List
tupleContoh = ('hello', 1, 1, 3, True)
listContoh = list(tupleContoh)
print(listContoh)

# After editing, then you can convert data to tuple again
tupleContoh = tuple(listContoh)
print(tupleContoh)