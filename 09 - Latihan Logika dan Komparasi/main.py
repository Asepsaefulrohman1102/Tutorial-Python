# Latihan Logika dan komparasi

# Membuat gabungan area rentang dari angka

# ++++3-----------10+++++++++

inputUser = float(input("Masukkan angka yang bernilai\nkurang dari 3 \natau \nlebih dari 10 \n: "))

# +++++3---------
# memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print("Angka kurang dari 3 : ", isKurangDari)

# -------10++++
# memeriksa angka lebih dari 10
isLebihDari = (inputUser > 10)
print("Angka lebih dari 10 : ", isLebihDari)

# +++++3---------10++++

isCorrect = (isKurangDari or isLebihDari)
print("Angka kurang dari 3 atau lebih dari 10 : ", isCorrect)


# -----3++++++10-----
# Kasus Irisan
print("\n",10*"=","\n")
inputUser = float(input("Masukkan angka yang bernilai\nlebih dari 3 \ndan \nkurang dari 10 \n: "))

# ---3+++++++
# lebih dari 3
isLebihDari = (inputUser > 3)
print("Angka lebih dari 3 : ", isLebihDari)

# +++++++10-----
# kurang dari 10
isKurangDari = (inputUser < 10)
print("Angka kurang dari 10 : ", isKurangDari)

# -----3++++++10-----
isCorrect = (isKurangDari and isLebihDari)
print("Angka kurang dari 3 atau lebih dari 10 : ", isCorrect)


# TUGAS 1
print("===TUGAS 1===\n")
InputUser = float(input(
    "Masukkan angka yang bernilai\nantara 0 sampai 5\ndan\nantara 8 sampai 11\n:"))

islebihdari = InputUser > 0
print("Lebihdari 0 =", islebihdari)

iskurangdari = InputUser < 5
print("Kurangdari 5 = ", iskurangdari)

isCorrect1 = iskurangdari and islebihdari

islebihdari = InputUser > 8
print("Lebihdari 8 =", islebihdari)

iskurangdari = InputUser < 11
print("Kurangdari 11 = ", iskurangdari)

isCorrect2 = iskurangdari and islebihdari

isCorrect3 = isCorrect1 or isCorrect2
print("Angka yang anda masukkan = ", isCorrect3)

# TUGAS 2
print("===TUGAS 2===\n")
InputUser = float(input(
    "Masukkan angka yang bernilai\nkurang dari 0\natau\nnantara 5 sampa1 8\natau\nlebih dari 11\n:"))

iskurangdari = InputUser < 0
print("Kurangdari 0 =", iskurangdari)

islebihdari = 5 < InputUser < 8
print("Lebihdari 5 = ", islebihdari)

isCorrect1 = iskurangdari or islebihdari

iskurangdari = 5 < InputUser < 8
print("Kurang 8 =", iskurangdari)

islebihdari = InputUser > 11
print("Lebihdari 11 = ", islebihdari)

isCorrect2 = iskurangdari or islebihdari

isCorrect3 = isCorrect1 or isCorrect2
print("Angka yang anda masukkan = ", isCorrect3)
