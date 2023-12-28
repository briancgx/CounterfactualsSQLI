import pandas as pd
df = pd.read_csv('Maligno_y_Benigno.csv')
columna_sentencias = df['Sentence']
arreglo_palabras = columna_sentencias.str.split().tolist()
print(arreglo_palabras)