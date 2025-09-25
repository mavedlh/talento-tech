# tupla vacia

tupla_vacia = ()
# tupla con numeros
t_numeros = (1, 2, 3, 4, 5)
# tupla mixta
t_mixta = (1, 3, "hola", 3.14)
# tuplaa aninada
t_anidada = (1, (2, 3), (4, 5))
# tupla de un solo elemento
t_uno = (34,)
# extracion de elementos de las tuplas
print(t_numeros[0])
print(t_anidada[1])
print(t_anidada[1:])
print(t_anidada[2])
t_anidada2 = (2, (4, 7, 9), (5, 6))
print(t_anidada2[1][2])
