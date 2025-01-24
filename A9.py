import random
def adivina_el_numero():
    numero_secreto = random.randint(1, 50)
    print("¡Bienvenido al juego de adivinanza!")
    print("He escogido un número entre 1 y 50. ¿Puedes adivinar cuál es?")
    intento = None
    while intento != numero_secreto:
        intento = int(input("Introduce tu adivinanza: "))
        if intento < numero_secreto:
            print("Más alto")
        elif intento > numero_secreto:
            print("Más bajo")
        else:
            print("¡Felicidades! Has adivinado el número.")
adivina_el_numero()
