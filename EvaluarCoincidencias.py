import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('new_dataset.csv')
columna_sentencias = df['SentenciaConvertida']
conteo = df['SentenciaConvertida'].value_counts()
conteo.to_csv('Frecuencias_features.csv', index=False)
print("\nConteo de frecuencia:")
print(conteo)
conteo.plot(kind='bar', color='skyblue')

# Agregar etiquetas y título
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.title('Frecuencia de Valores en Columna1')

# Mostrar el gráfico
plt.show()