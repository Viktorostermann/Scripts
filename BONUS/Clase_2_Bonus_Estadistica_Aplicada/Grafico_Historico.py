import seaborn as sns
import matplotlib.pyplot as plt


datos = sns.load_dataset('iris')

# print(data)


#Histograma
sns.histplot(datos['sepal_length'],bins=5)
plt.title('Histograma de longitud del sepalo')
plt.show()
