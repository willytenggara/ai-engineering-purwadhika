# Conditional Statements Explanation

# Contoh 1
nilai = 90
if nilai > 80:
  grade = 'Baik'
  status = "Lulus"
else: 
  grade = "Kurang Baik"
  status = "Tidak Lulus"
# print(status)


# Contoh 2
nilai = input("Masukkan nilai: ")
nilai = int(nilai)
if nilai > 80:
  grade = "A"  
elif nilai > 70: 
  grade = "B"
else: 
  grade = "C"

print(grade)