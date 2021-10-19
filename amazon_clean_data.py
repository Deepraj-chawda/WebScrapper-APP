import pandas as pd

class Clean:

    def rating(self,data):
        return data['Rating'].apply(lambda rate : float(rate.split(' ')[0]))

    def price(self,data):
        return data['price'].apply(lambda p : float(p[1:].replace(',','')))

    def original_price(self,data):
        return data['Original_price'].apply(lambda p : float(p[1:].replace(',','')))

    def fun(self,row):

        s = row.split(' ')
        try:
            saves = float(s[1][1:].replace(',', ''))
        except:
            saves = None
        return saves

    def save(self,data):
        return data['Discount'].apply(self.fun)