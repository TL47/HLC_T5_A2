n1 = int(input("Introduce el primer número: "))
n2 = int(input("Introduce el segundo número: "))
n3 = int(input("Introduce el tercer número: "))
if n1 > n2 and n1 > n3 and n2 != n3:
    print("El mayor número es: ", n1)
elif n2 > n1 and n2 > n3:
    print("El mayor número es: ", n2)
elif n3 > n1 and n3 > n2:
    print("El mayor número es: ", n3)
elif n1 == n2 == n3:
    print("Todos los números son iguales.")
elif n1 == n2:
    print("Hay un empate entre el primer y segundo número: ", n1)
elif n1 == n3:
    print("Hay un empate entre el primer y tercer número: ", n1)
elif n2 == n3:
    print("Hay un empate entre el segundo y tercer número: ", n2)