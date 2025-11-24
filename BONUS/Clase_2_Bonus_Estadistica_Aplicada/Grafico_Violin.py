import seaborn as sns
import matplotlib.pyplot as plt


datos = sns.load_dataset('iris')

# print(data)

#grafico de violin

sns.violinplot(data=datos,x='species',y='sepal_length')
plt.title('Grafico de violin')
plt.show()

sns.pairplot(data=datos,hue='species')
plt.show()