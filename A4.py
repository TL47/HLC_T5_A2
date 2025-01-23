def check_pass():
    system_pass = "secreta123"
    tries = 0

    while tries < 3:
        user_pass = input("Introduce tu contraseña")
        if system_pass == user_pass:
            print("Bienvenido")
            break
        tries += 1

check_pass()