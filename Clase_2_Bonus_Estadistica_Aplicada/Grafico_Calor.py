import seaborn as sns
import matplotlib.pyplot as plt

# Cargar dataset iris
datos = sns.load_dataset('iris')

# Pairplot
sns.pairplot(data=datos, hue='species')
plt.show()

# Heatmap solo con columnas numéricas
corr = datos.select_dtypes(include='number').corr() # heatmap solo con columnas numéricas
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Mapa de calor de las correlaciones')
plt.show()


# Codigo original con error en columna categórica que significa el tipo de flor y da error al hacer el heatmap
'''sns.pairplot(data=datos,hue='species')
plt.show()

#heatmap
corr=datos.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm') # heatmap con todas las columnas (Da error porque hay una columna categórica que no se puede graficar)
plt.title('Mapa de calor de las correlaciones')
plt.show()'''
