import seaborn as sns
import matplotlib.pyplot as plt


datos = sns.load_dataset('iris')

# print(data)

'''# grafico de dispersion
sns.scatterplot(data=datos,x='sepal_length',y='sepal_width')
plt.title('Grafico de dispersion de longitud del sepalo vs ancho')
plt.xlabel='sepal_length'
plt.ylabel='sepal_width'
plt.show()'''

'''#Grafico de Barras
sns.barplot(data=datos,x='species',y='sepal_length')
plt.title('Grafico de barras longitud del sepalo por especie')
plt.xlabel='Specie'
plt.ylabel='sepal_length'
plt.show()'''

'''#Histograma
sns.histplot(datos['sepal_length'],bins=5)
plt.title('Histograma de longitud del sepalo')
plt.show()'''

'''#grafico de violin
sns.violinplot(data=datos,x='species',y='sepal_length')
plt.title('Grafico de violin')
plt.show()'''


# Pairplot
sns.pairplot(data=datos, hue='species')
plt.show()

# Heatmap solo con columnas numéricas
corr = datos.select_dtypes(include='number').corr() # heatmap solo con columnas numéricas
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Mapa de calor de las correlaciones')
plt.show()


# Heatmap con todas las columnas (Da error porque hay una columna categórica que no se puede graficar)
'''sns.pairplot(data=datos,hue='species')
plt.show()

#heatmap
corr=datos.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm') # heatmap con todas las columnas (Da error porque hay una columna categórica que no se puede graficar)
plt.title('Mapa de calor de las correlaciones')
plt.show()'''
