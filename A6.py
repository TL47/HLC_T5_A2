def check_chars():
    word = input("Introduce la palabra:")
    special_chars = ["@", "#", "$", "%"]

for char in special_chars:
    if char in word:
        print("La palabra tiene el caracter", char)

check_chars()