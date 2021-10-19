import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from amazon_clean_data import Clean

class Visual:
    def __init__(self):
        plt.rcParams['figure.figsize'] = [15, 15]
        plt.style.use('classic')


    def price_graph(self,data_v):
        plt.figure(dpi=65)

        bar = sns.barplot(y='Brand', x='Price', data=data_v[:100])
        plt.grid(which='both', axis='both')

        plt.show()

    def original_price_graph(self,data_v):

        plt.figure(dpi=60)
        bar = sns.barplot(y='Brand', x='Original_price', data=data_v[:100])
        plt.grid(which='both', axis='both')

        plt.show()

    def rating_graph(self,data_v):

        plt.figure(dpi=65)
        bar = sns.barplot(y='Brand', x='Rating', data=data_v[:100])
        plt.grid(which='both', axis='both')

        plt.show()

    def discount_graph(self,data_v):

        plt.figure(dpi=65)
        bar = sns.barplot(y='Brand', x='Discount', data=data_v[:100])
        plt.grid(which='both', axis='both')

        plt.show()


if __name__ == '__main__':

    data = pd.read_excel('shoes.xlsx')
    v = Visual()
    v.price_graph(data)
    v.original_price_graph(data)
    v.rating_graph(data)
    v.discount_graph(data)