#diccionario anidado simple 
dper={"nombre":"Maria",
         "apellido":"De la hoz Viaña",
         "edad":25,
         "direccion":{
           "CALLE": "51",
           "numero":"57 27",
           "localidad":"Soledad",
           "ciudad":"Bogota"
           }
         }
print("\ndiccionario anidado simple:")
print(dper["direccion"]["ciudad"])
#modificar o agregar valores al diccionario
dper["edad"]=25 #MODIFICAR
dper["direccion"]["localidad"]="engativa"
dper["profesion"]="asesora" #agregar
dper["direccion"]["pais"]="colombia" #agregar
print("\nmodificar o agregar valores al diccionario:")
print(dper)

#diccionarios de diccionarios 
est={
    "001":{"nombre1":"Pepito", "nota":2.9},
    "002":{"nombre2":"Juanita","nota":3.1},
    "003":{"nombre3":"Pedro", "nota":4.7}
}
print("\ndiccionarios de diccionarios:")
print(est["002"]["nombre2"])
#diccionarios con listas dentro
empresa={
    "departamento":{
        "Tec":["ana","luisa","pedro"],
        "RRHH":["martha","maria"],
        "Ventas":["luis","elena"]
    }
}
print("\ndiccionarios con listas dentro:")
print(empresa["departamento"]["Tec"][2])#acceder a pedro
    
