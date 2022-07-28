# belajar casting
# merubah dari satu tipe ke tipe lain
# tipe data = int, float, string, boolean

## ini adalah integer
data_int = 9; 
print("data =", data_int, "tipe data =", type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) # akan false jika nilai int = 0
print("data =", data_float, "tipe data =", type(data_float))
print("data =", data_str, "tipe data =", type(data_str))
print("data =", data_bool, "tipe data =", type(data_bool))

## Float
print("=== Float ===")
data_float = 9.5;
print("data =", data_float, "tipe data =", type(data_float))

data_int = float(data_float) # akan dibulatkan ke bawah
data_str = str(data_float)
data_bool = bool(data_float)  # akan false jika nilai float = 0
print("data =", data_float, "tipe data =", type(data_float))
print("data =", data_str, "tipe data =", type(data_str))
print("data =", data_bool, "tipe data =", type(data_bool))


## Boolean
print("/n")
print("=== Boolean ===")
data_bool = True;
print("data =", data_bool, "tipe data =", type(data_bool))

data_int = int(data_bool)  # akan dibulatkan ke bawah
data_str = str(data_bool)
data_float = float(data_bool)  # akan false jika nilai bool = 0
print("data =", data_int, "tipe data =", type(data_int))
print("data =", data_str, "tipe data =", type(data_str))
print("data =", data_bool, "tipe data =", type(data_bool))

## Float
print("=== str ===")
data_str = "Hello world"
print("data =", data_str, "tipe data =", type(data_str))

""" data_int = int(data_str)  # strng harus angka """
""" data_str = str(data_str)  # strng harus angka """
data_bool = bool(data_str)  # akan false jika string kosong
""" print("data =", data_int, "tipe data =", type(data_int))
print("data =", data_float, "tipe data =", type(data_float)) """
print("data =", data_bool, "tipe data =", type(data_bool))
