# bucle while
import random


contador = 1
while contador <= 100:
    print("numero:", contador)
    contador += 1  # modificar el contador


numero = 0
while numero != 7:
    numero = random.randint(1, 10)
    print("salio:", numero)
# bucle for
frutas = ["manzana", "pera", " banano", "durazno"]
for fruta in frutas:
    print("me gusta la", fruta)
# bucle break
for numero in range(1, 10):
    if numero == 5:
        print("se encontro el numero 5, se detiene el bucle")
    break
print("numero", numero)
# bucle continue
for numero2 in range(1, 20):
    if numero2 % 2 == 0:
        continue
    print("numero impar:", numero2)
    # bucle pass
    contador1 = 0
    while contador1 < 5:
        contador1 += 1
        pass
    # con for
