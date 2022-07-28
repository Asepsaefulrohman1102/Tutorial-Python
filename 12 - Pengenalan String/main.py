data = "Hello World"	
print(data)
print(type(data))
# 1. Cara membuat string

""" 
    1. dengan menggunakan single quote '---'
    2. dengan menggunakan double quote "---"
"""

data = 'Hello World dengan single quote'	
print(data)

data = "Hello World dengan double quote "	
print(data)

print('"Halo, apa kabar?"')
print("'Halo, apa kabar?'")
print("ini adalah hari jum'at")

# 2. menggunakan tanda \

# membuat tanda ' menjadi string
print('mari shalat jum\'at')
print('g\'day, isn\'t it?')	

# backlash
print("C:\\Users\\User\\Desktop")

# TAB
print("dia semakin jauh\t\tdari saya")

# BACKSPACE
print("dia semakin jauh\b\b\b\bdari saya")

# NEWLINE
print("dia semakin jauh\ndari saya") # LF -> Line Feed
print("dia semakin jauh\rdari saya") # CR -> Carriage Return
print("dia semakin jauh\r\ndari saya") # CRLF -> Carriage Return Line Feed

# 3. STRING LITERAL ATAU RAW

# HATI-HATI
print("C:\\Users\\User\\Desktop") # akan salah pathnya

# MENGGUNAKAN RAW STRING
print(r"C:\Users\User\Desktop") # AKAN BENAR

# MULTILINE STRING
print("""
      Nama : Asep
      Kelas : 4216
      """)

# MULTILINE LITERAL STRING DAN RAW
print(r"""
      Nama : Asep
      Kelas : 4216
      Website : www.google.com
      """)
