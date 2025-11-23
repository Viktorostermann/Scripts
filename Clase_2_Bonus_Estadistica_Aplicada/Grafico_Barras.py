import seaborn as sns
import matplotlib.pyplot as plt


datos = sns.load_dataset('iris')

# print(data)

#Grafico de Barras
sns.barplot(data=datos,x='species',y='sepal_length')
plt.title('Grafico de barras longitud del sepalo por especie')
plt.xlabel='Specie'
plt.ylabel='sepal_length'
plt.show()
