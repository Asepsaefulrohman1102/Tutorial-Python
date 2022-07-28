# Operasi Aritmatika

from re import X


a = 10
b = 3

# Operasi Tambah
hasil = a + b
print(a, "+",b,"Hasil Penjumlahan:", hasil)

# Operasi Kurang
hasil = a - b
print(a, "-",b,"Hasil Pengurangan:", hasil)

# Operasi kali
hasil = a * b
print(a, "*",b,"Hasil Perkalian:", hasil)

# Operasi bagi
hasil = a / b
print(a, "/",b,"Hasil Pembagian:", hasil)

# Operasi Eksponen (pangkat)
hasil = a ** b
print(a, "**",b,"Hasil Pangkat:", hasil)

# Operasi Modulus
hasil = a % b
print(a, "%",b,"Hasil Modulus:", hasil)

# Operasi Floor Division
hasil = a // b
print(a, "//",b,"Hasil Floor Division:", hasil)

# Prioritas Operasi
"""     
    1. ()
    2. eksponen **
    3. perkalian dan teman-teman * / ** % //
    4. pertambahan dan pengurangan + -
 """
x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x, "Hasil :", hasil)

hasil = x + y * z
print(x,'+',y,'*',z,'Hasil :', hasil) 
# kurung akan mengambil langkah paling pertama

hasil = (x + y) * z
print('(',x, '+', y,')', '*', z, 'Hasil :', hasil)
