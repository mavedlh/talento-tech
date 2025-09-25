# 1. Argumento posicional
def presentar(nombre, edad):
    print(f"{nombre}tiene {edad} años. ")


presentar("paola", 30)  # Correcto
# presentar("paola") #Error: falta argumento edad.
# w. Argumentos de palabras claves o keywords
presentar(edad=30, nombre="Ivon")


# 3. Argumentos predeterminados o default
def saludar(nombre, saludo="hola"):
    print(f"{saludo},{nombre}")


saludar("paola")
saludar("luis", "hey")

# 3Argumentos de longitud variable
# se usan cuando no sabemos cuantos argumentos recibiran la funcion


# args=junta argumentos de una tupla
# kwargs=junta argumentos nombrados en un diccionario
def mostrar_datos(*args, **kwargs):
    print("args(tupla)", args)
    print("kwargs(diccionario):", kwargs)

    mostrar_datos(2, 3, 4, nombre="Paola", edad=30)


# Ejercisios
# Ejercisios 1 Area del circulo
import math


def area_circulo(radio):
    return math.pi * radio**2


print(area_circulo(5))


def celsius_a_farenheit(celsius):
    return (celsius * 9 / 5) + 32


print(celsius_a_farenheit(30), "Grados Farenheit")

#  ejercisios 3 calcular la propina 10%


def propina(valor_total, porcent_propina=10):
    return valor_total * (porcent_propina / 100)


print(propina(100000))


# Ejercisio 4 promedio de calificaciones
def promedio(notas):
    return sum(notas) / len(notas)


print(promedio([3.5, 4.0, 5.0, 3.0]))
# ejercicio 5 verificaciones contraseña segura


def contrasena_segura(contrasena):
    if len(contrasena) < 8:
        return False

    tiene_digito = any(c.isdigit() for c in contrasena)  # any=Alguno #c=Evalua cada caracter
    tiene_mayuscula = any(c.isupper() for c in contrasena)  # fase 3. Al menos una mayuscula
    tiene_caracter_especial = any(not c.isalnum() for c in contrasena)  # Fase 4 al menos un caracter especial
    return tiene_digito and tiene_mayuscula and tiene_caracter_especial


print(contrasena_segura("aabbwqs1*"))


# Verificacion contraseña con mensaje de error
def validar_contrasena(contrasena2):
    errores = []  # Fase1. se crea una lista
    if len(contrasena2) < 8:
        errores.append(
            "debe tener al menos 8 caracteres. "
        )  # appemd: se agrega caracter o valor al final #Windows + . emojies.

    if not any(c.isdigit() for c in contrasena2):  # fase 2 mostrar al menos un digito
        errores.append("Debe tener al menos un numero")

    if not any(c.isupper() for c in contrasena2):  # fase 3. Al menos una mayuscula
        errores.append("Debe tener al menos una letra en mayuscula")

    if not any(not c.isalnum() for c in contrasena2):  # fase 4 Al menos un caracter especial
        errores.append("Debe tener un caracter especial (ej:q,!,$,%,&,*).")
    if not errores:
        return True, ["Contraseña segura"]
    else:
        return False, errores


print(validar_contrasena("AAAfg789_"))
