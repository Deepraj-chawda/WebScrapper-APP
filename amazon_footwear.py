import bs4
import requests
import pandas as pd

class scrap_footwear:
    def __init__(self):
        self.header = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.5',
            'Host': 'www.amazon.in',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'
        }
        self.url = 'https://www.amazon.in/s?k={}&page={}&qid=1627636153&ref=sr_pg_{}'

    def scrap(self,category,page_no):
        footwear = {
            'Brand': [],
            'Category': [],
            'Rating': [],
            'price': [],
            'Original_price': [],
            'Discount': []
        }


        response = requests.get(self.url.format(category, page_no,page_no), headers=self.header)
        soup = bs4.BeautifulSoup(response.content, 'html.parser')

        if response.status_code == 200:

            divs = soup.find_all('div', attrs={
                    'class': 'sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col sg-col-4-of-20'})

            for div in divs:
                product = div.find('div', attrs={'class': 'a-section a-spacing-none'})

                try:
                    if product.find('div', attrs={'class': "a-row a-size-small"}).span.text.strip():
                        pass
                    price = product.find_all('span', attrs={'class': "a-offscreen"})
                    if price[1].text.strip():
                        pass
                except:
                    continue

                footwear['Brand'].append(product.find('h5', attrs={'class': "s-line-clamp-1"}).text.strip())
                footwear['Category'].append(product.find('h2', attrs={
                        'class': "a-size-mini a-spacing-none a-color-base s-line-clamp-2"}).text.strip())
                footwear['Rating'].append(product.find('div', attrs={'class': "a-row a-size-small"}).span.text.strip())
                price = product.find_all('span', attrs={'class': "a-offscreen"})
                footwear['price'].append(price[0].text.strip())
                footwear['Original_price'].append(price[1].text.strip())
                footwear['Discount'].append('Save ' + product.find('div', attrs={
                        'class': 'a-row a-size-base a-color-base'}).text.split('Save')[-1].strip())


        else:
            print(response.status_code, 'Reason :', response.reason)

        footwear = pd.DataFrame(footwear)

        return footwear

if __name__ == '__main__':
    amazon = scrap_footwear()
    footwear = amazon.scrap('shoes',3)
    #footwear.to_excel('1.xlsx',engine='xlsxwriter')
    print(footwear)
