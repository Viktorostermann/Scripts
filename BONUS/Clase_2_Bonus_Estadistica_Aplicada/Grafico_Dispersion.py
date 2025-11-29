import seaborn as sns
import matplotlib.pyplot as plt


datos = sns.load_dataset('iris')

# print(data)

# grafico de dispersion

sns.scatterplot(data=datos,x='sepal_length',y='sepal_width')
plt.title('Grafico de dispersion de longitud del sepalo vs ancho')
plt.xlabel='sepal_length'
plt.ylabel='sepal_width'
plt.show()