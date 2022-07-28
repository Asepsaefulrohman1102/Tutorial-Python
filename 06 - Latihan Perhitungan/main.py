# Latihan Konversi Satuan Temperature

# Program konversi suatu nilai temperature dari suatu satuan ke suatu satuan lain

print("PROGRAM KONVERSI TEMPERATURE/n")

celcius = float(input("Masukkan nilai temperature dalam celcius: "))
print("Nilai temperature dalam celcius: ", celcius, "Celcius")

# Reamur
# Reamur = Celcius * 4/5
reamur = (4 / 5) * celcius
print("Nilai temperature dalam reamur: ", reamur, "Reamur")

# Fahrenheit
fahrenheit = (9 / 5) * celcius + 32
print("Nilai temperature dalam fahrenheit: ", fahrenheit, "Fahrenheit")

# Kelvin
kelvin = celcius + 273.15
print("Nilai temperature dalam kelvin: ", kelvin, "Kelvin")

Fahrenheit = float(input("Masukkan suhu dalam Fahrenheit :"))
Celcius = ((5/9) * Fahrenheit) - 32
Kelvin = Celcius + 273
print("suhu dalam Kelvin =", Kelvin, "Kelvin")

Kelvin = float(input("Masukkan suhu dalam Kelvin :"))
Celcius = Kelvin - 273
Fahrenheit = ((9/5) * Celcius) + 32
print("suhu dalam Fahrenheit =", Fahrenheit, "Fahrenheit")
