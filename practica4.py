#diccionario anidado simple
dper={
    "nombre":"Elias",
         "apellido":"Gamez",
         "edad":18,
         "direccion":{
           "CALLE": "51",
           "numero":"57 27",
           "localidad":"Soledad",
           "ciudad":"Bogota"
           }
}
print(dper)

#diccionario de diccionarios
est={
    "N1":{"nombre1":"Nena", "nota":10.10},
    "M2":{"nombre2":"Milo","nota":99.80},
    "N3":{"nombre3":"Niña", "nota":99.99}
}
print("\ndiccionarios de diccionarios")
print(est)

#diccionarios con listas dentro
Restaurante={
      "chef":["Jesu","Mary","Isa"],
      "MDA":["Val","Cam"],
      "Ventas":["elias","Milo"]
}
print("\ndiccionarios con listas dentro")
print(Restaurante["chef"])


#CONJUNTOS 
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
C = {7, 8, 9}
D = {10, 11}

# Eliminaciones
A.remove(2)  
B.remove(5)  

# Adiciones
C.add(12)    
D.add(13)    
print("Conjunto A:", A)
print("Conjunto B:", B)
print("Conjunto C:", C)
print("Conjunto D:", D)



    

