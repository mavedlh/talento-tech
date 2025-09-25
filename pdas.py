# crear un array en numpy
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)
# operaciones vectorizadas
print(arr * 2)
print(np.mean(arr))
# Crea unn diafragma con pandas
import pandas as pd

data = {"Nombre": ["ana", "Lucia", "Carlos"], "Edad": [23, 34, 45], "Ciudad": ["Madrid", "Barcelona", "Valencia"]}
df = pd.dataFrame(data)
print(df)
# Filtrar por edad >25
print(df[df["edad"] > 25])
# vector
import numpy as np

vector = np.array([2, 5, 7])
print(vector)

# Array 20
array2 = np.array([[1, 2, 3], [4, 5, 6]])
print(array2)

# Matriz
matriz = np.array([[2, 4, 6], [8, 10, 12]])
print(matriz.shape)
