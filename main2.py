import requests
from bs4 import BeautifulSoup
import csv
import openpyxl
import re


fieldnames = ['Collection Name', 'Product Title', 'Product Images Link', 'Product Price', 'Discounted Price',
              'Tags', 'Product Description']

# csvfile = open(f'/Users/navepno/prod/gumstuffscrapping/second.csv', 'w', newline='')
# writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
# writer.writeheader()
csvfile = open(f'/Users/navepno/prod/gumstuffscrapping/second1.csv', 'a', newline='')
writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
url = "https://www.tropicanawholesale.com/shop-by-brand/"

headers = {
    'User-Agent': 'whatever',
    'From': 'navepnoe@gmail.com'  # This is another valid field
}
content = requests.get(url, headers=headers)

soup = BeautifulSoup(content.text, 'html.parser')

brand_list = []
brand_item = soup.find_all("div", {"class": "category-item"})

for item in brand_item:
    brand_list.append(item.find("a")['href'])

# print(brand_list)

for brand in brand_list[149:]:
    url = "https://www.tropicanawholesale.com" + brand
    headers = {
        'User-Agent': 'whatever',
        'From': 'navepnoe@gmail.com'  # This is another valid field
    }
    content = requests.get(url, headers=headers)

    soup = BeautifulSoup(content.text, 'html.parser')
    products = soup.find_all("div", {"class": "product-name"})
    # product
    for product in products:
        product_link = product.find("a")['href']
        url = "https://www.tropicanawholesale.com" + product_link

        cookies = {
            'App.RecentlyViewedProducts - /': '14243',
            'ASP.NET_SessionId': 'nrtnktozltqegkl5x341i5cr',
            'Retail.CookiePolicy - /': '02/04/2023 08:49:31',
            '_ga': 'GA1.2.495848635.1680421773',
            '_gid': 'GA1.2.120224517.1680421773',
            '_gat_UA-117112626-1': '1',
            'App.Authentication - /': 'earyox0vv00macejfu2j2lxw',
            'App.Session - /': '0ella0vq5g1lezxdkkav40zd',
            '__atuvc': '2%7C14',
            '__atuvs': '6429338cfa551d9b001',
        }

        headers = {
            'authority': 'www.tropicanawholesale.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,fr;q=0.6',
            'cache-control': 'max-age=0',
            # 'cookie': 'App.RecentlyViewedProducts - /=14243; ASP.NET_SessionId=nrtnktozltqegkl5x341i5cr; Retail.CookiePolicy - /=02/04/2023 08:49:31; _ga=GA1.2.495848635.1680421773; _gid=GA1.2.120224517.1680421773; _gat_UA-117112626-1=1; App.Authentication - /=earyox0vv00macejfu2j2lxw; App.Session - /=0ella0vq5g1lezxdkkav40zd; __atuvc=2%7C14; __atuvs=6429338cfa551d9b001',
            'referer': 'https://www.tropicanawholesale.com/login?redirectto=/shop-by-brand/Snickers/Snickers-Hi-Protein-Bars-12x55g/',
            'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36',
        }

        content = requests.get(url, cookies=cookies, headers=headers)

        soup = BeautifulSoup(content.text, 'html.parser')
        product_name = soup.find("h1", {"class": "product-name"}).find_all(string=True, recursive=False)[0]
        print(product_name)
        try:
            product_image = soup.find("div", {"class": "main-image"}).find("a")['href']
            product_image = 'https://www.tropicanawholesale.com' + product_image
        except:
            product_image = ''
        product_prices = soup.find_all("div", {"class": "product-prices"})
        product_barcodes = soup.find_all("div", {"class": "product-code"})
        try:
            product_description = soup.find("div", {"class": "product-description"}).find_all(string=True, recursive=False)[0]
        except:
            product_description = ''


        for i in range(len(soup.find_all("div", {"class": "product-code"}))):
            product_code = soup.find_all("div", {"class": "product-code"})[i].find_all(string=True, recursive=False)[0]
            product_additional_name = soup.find_all("div", {"class": "product-sizeflavour"})[i].find_all(string=True, recursive=False)[0]
            # product_discount_price = discount_prices[i]
            try:
                product_retail_price = soup.find("div", {"class": "was-price"}).find_all(string=True, recursive=False)[0].split('Standard price')[-1]
            except:
                product_retail_price = ''
            product_discount_price = product_prices[i].find("div").find_all(string=True, recursive=False)[0].split('Your price')[-1]
            product_barcode = product_barcodes[i].find_all(string=True, recursive=False)[0]
            # print(product_additional_name + '=-=-=-=-=-' + product_code + '=-=-=-=-=-' + product_discount_price, end='\n\n\n')
            # if i % 2 == 1:
            #     try:
            #         product_barcode = product_barcodes[i].find_all(string=True, recursive=False)[0]
            #         product_barcode = int(product_barcode)
            #     except:
            #         product_barcode = ''
            # else:
            #     try:
            #         product_barcode = product_barcodes[i + 1].find_all(string=True, recursive=False)[0]
            #         product_barcode = int(product_barcode)
            #     except:
            #         product_barcode = ''
            # print(product_barcode)
            # print(url, end='\n\n\n')

            # csvfile = open(f'/Users/navepno/prod/gumstuffscrapping/second.csv', 'a', newline='')
            # writer = csv.DictWriter(csvfile, fieldnames=fieldnames)


            data = {
                'Collection Name': '',
                'Product Title': '',
                'Product Images Link': '',
                'Product Price': '',
                'Discounted Price': '',
                'Tags': '',
                'Product Description': '',
            }

            # fieldnames = ['Collection Name', 'Product Title', 'Product Images Link', 'Product Price',
            #               'Discounted Price',
            #               'Tags', 'Product Description']

            try:
                data['Collection Name'] = product_name
            except:
                data['Collection Name'] = ''

            try:
                data['Product Title'] = product_additional_name
            except:
                data['Product Title'] = ''

            try:
                data['Product Price'] = product_retail_price
            except:
                data['Product Price'] = ''

            try:
                data['Discounted Price'] = product_discount_price
            except:
                data['Discounted Price'] = ''

            try:
                data['Product Images Link'] = product_image
            except:
                data['Product Images Link'] = ''

            try:
                data['Product Description'] = product_description
            except:
                data['Product Description'] = ''

            try:
                data['Tags'] = product_barcode
            except:
                data['Tags'] = ''

            writer.writerow(data)
            print(url)
            print('ok')







csvfile.close()











            # print(product_bracode)
            # print(url, end='\n\n\n')
            # if 'Your price' in product_price:
            #     product_discount_price = product_price
            #     print(product_discount_price)
    # print(products)

