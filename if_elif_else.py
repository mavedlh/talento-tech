#if else 
ahorro= float(input("¿cuanto dinero tienes ahorrado?"))
if ahorro >= 500000:
    print("¡muy bien! Tienes suficiente dinero para ivertir.")
else:
    print("necesitas ahorrar un poco mas antes de invertir ")

#ejemplo 2 
ingresos= float(input("¿cuanto son tus ingresos mensuales $ "))
gastos= float (input ("ingresa tus gastos mensuales"))
if ingresos > gastos:
    print("¡felicidades!estas generando ahorro ")
else:
    print("cuidado, estas gastando mas de lo que ganas ")

#ejemplo 3
nota=float(input("¿cuanto sacaste en el parcial?"))
if nota > 3.5:
    print("excelente, has aprobado el curso")
else:
    print("debes repetir el curso")
