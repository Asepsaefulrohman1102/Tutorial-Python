# Operasi yang dapt dilakukan dengan penyingkatan
# Operasi yang dapat dilakukan dengan penambahan assigment

a = 5 # adalah assignment
print("nilai a = ", a)

a += 1 # artinya adalah a = a + 1
print("nilai a += 1, nilai a menjadi : ", a)

a -= 2 # artinya adalah a = a - 2
print("nilai a -= 2, nilai a menjadi : ", a)

a *= 5 # artinya adalah a = a * 5
print("nilai a *= 5, nilai a menjadi : ", a)

a /= 2 # artinya adalah a = a / 2
print("nilai a /= 2, nilai a menjadi : ", a)

b = 10 # adalah assignment
print("\nnilai b = ", b)

b %= 3 # artinya adalah b = b % 3
print("nilai b %= 3, nilai b menjadi : ", b)

b = 10 # adalah assignment
print("\nnilai b = ", b)

b //= 3 # artinya adalah b = b // 3
print("nilai b //= 3, nilai b menjadi : ", b)

a = 5 # adalah assignment
print("\nnilai a = ", a)

a **= 3 # artinya adalah a = a ** 3
print("nilai a **= 3, nilai a menjadi : ", a)


# Operasi bitwise
c = True # adalah assignment
print("\nnilai c = ", c)

c |= False # artinya adalah c = c | False
print("nilai c |= False, nilai c menjadi : ", c)

c = False  # adalah assignment
print("\nnilai c = ", c)

c |= False  # artinya adalah c = c | False
print("nilai c |= False, \nnilai c menjadi : ", c)

# AND
c = True
print("\nnilai c = ", c)
c &= False
print("nilai c &= False, nilai c menjadi : ", c)
c = True
print("\nnilai c = ", c)
c &= True
print("nilai c &= True, nilai c menjadi : ", c)

# XOR
c = True
print("\nnilai c = ", c)
c ^= False
print("nilai c &= False, nilai c menjadi : ", c)
c = True
print("\nnilai c = ", c)
c ^= True
print("nilai c &= True, nilai c menjadi : ", c)

# get bit
d = 0b0100
print("\nnilai d = ",format(d, '04b'))
d >>= 2
print("nilai d >>= 2, nilai d menjadi : ", format(d, "04b"))	
d <<= 1
print("nilai d >>= 1, nilai d menjadi : ", format(d, "04b"))
