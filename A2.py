n1 = int(input("Introduce el primer número"))
n2 = int(input("Introduce el segundo número"))
n3 = int(input("Introduce el tercer número"))
if n1 > n2 and n1 > n3:
    print("El número mayor es" + n1)
elif n2 > n1 and n2 > n3:
    print("El número mayor es" + n2)
else:
    print("El número mayor es:" + n3)