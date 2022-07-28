# Operasi Komparasi

# Setiap hasil dari operasi komparasi adalah boolean

# >, <, >=, <=, ==, !=, is, is not

a = 4
b = 2

# Lebih besar dari
print("=== Lebih Dari ===")
hasil = a > 3
print(a,'>',3,':',hasil)
hasil = b > 3
print(b,'>',3,':',hasil)
hasil = b > 2
print(b,'>',2,':',hasil)

# kurang dari
print("=== Kurang Dari ===")
hasil = a < 3
print(a,'<',3,':',hasil)
hasil = b < 3
print(b,'<',3,':',hasil)
hasil = b < 2
print(b,'<',2,':',hasil)

# Lebih besar dari sama dengan
print("=== Lebih Dari sama dengan ===")
hasil = a >= 3
print(a,'>=',3,':',hasil)
hasil = b >= 3
print(b,'>=',3,':',hasil)
hasil = b >= 2
print(b,'>=',2,':',hasil)

# kurang dari
print("=== Kurang Dari sama dengan ===")
hasil = a <= 3
print(a,'<=',3,':',hasil)
hasil = b <= 3
print(b,'<=',3,':',hasil)
hasil = b <= 2
print(b,'<=',2,':',hasil)

# sama dengan (==)
print("=== sama dengan ===")
hasil = a == 4
print(a,'==',4,':',hasil)
hasil = b == 4
print(b,'==',4,':',hasil)

# tidak sama dengan (!=)
print("=== tidak sama dengan ===")
hasil = a != 4
print(a,'!=',4,':',hasil)
hasil = b != 4
print(b,'!=',4,':',hasil)

# is sebagai komparasi objek identity
print("=== Objek identity (is) ===")
x = 5 # ini adalah assigment membuat objek
y = 5
print("nilai x:",x, ',id = ', hex(id(x)))
print("nilai y:",y, ',id = ', hex(id(y)))
hasil = x is y
print("x is y =", hasil)

# is sebagai komparasi objek identity
x = 5  # ini adalah assigment membuat objek
y = 6
print("nilai x:", x, ',id = ', hex(id(x)))
print("nilai y:", y, ',id = ', hex(id(y)))
hasil = x is y
print("x is y =", hasil)

print("=== Objek identity (is not) ===")
x = 5  # ini adalah assigment membuat objek
y = 5
print("nilai x:", x, ',id = ', hex(id(x)))
print("nilai y:", y, ',id = ', hex(id(y)))
hasil = x is not y
print("x is y =", hasil)

# is sebagai komparasi objek identity
x = 5  # ini adalah assigment membuat objek
y = 6
print("nilai x:", x, ',id = ', hex(id(x)))
print("nilai y:", y, ',id = ', hex(id(y)))
hasil = x is not y
print("x is y =", hasil)
