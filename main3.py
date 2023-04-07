import requests
from bs4 import BeautifulSoup
import csv
import openpyxl
import re


fieldnames = ['Collection Name', 'Product Title', 'Product Images Link', 'Product Price', 'Discounted Price',
             'Product Description']

# csvfile = open(f'/Users/navepno/prod/gumstuffscrapping/second.csv', 'w', newline='')
# writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
# writer.writeheader()
csvfile = open(f'/Users/navepno/prod/gumstuffscrapping/third.csv', 'w', newline='')
writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
writer.writeheader()
url = "https://www.prolifedistribution.co.uk/brands"

headers = {
    'User-Agent': 'whatever',
    'From': 'navepnoe@gmail.com'  # This is another valid field
}
content = requests.get(url, headers=headers)

soup = BeautifulSoup(content.text, 'html.parser')

brand_list = []
brand_item = soup.find_all("a", {"class": "hasTooltip"})

for item in brand_item:
    brand_list.append(item["href"])

for brand in brand_list:
    url = "https://www.prolifedistribution.co.uk" + brand
    headers = {
        'User-Agent': 'whatever',
        'From': 'navepnoe@gmail.com'  # This is another valid field
    }
    content = requests.get(url, headers=headers)

    soup = BeautifulSoup(content.text, 'html.parser')
    products = soup.find_all("div", {"class": "product__details__title product__details__title--branded"})
    for product in products:
        product_link = product.find("a")['href']
        url = "https://www.prolifedistribution.co.uk" + product_link

        cookies = {
            'VSCurrency': 'GBP',
            'vsases.b98d': '*',
            '__ssds': '3',
            '_gid': 'GA1.3.1851888342.1680438934',
            '_hjFirstSeen': '1',
            '_hjSession_1195751': 'eyJpZCI6IjliOGM0MTNhLWI3N2ItNGU2Ny1hY2YxLWEzZDg2ZDc0MDQyNyIsImNyZWF0ZWQiOjE2ODA0Mzg5MzQ0MTIsImluU2FtcGxlIjpmYWxzZX0=',
            '_hjAbsoluteSessionInProgress': '1',
            '__ssuzjsr3': 'a9be0cd8e',
            '__uzmaj3': '088f78ca-6239-41af-84f0-28faccdbbf4d',
            '__uzmbj3': '1680438934',
            '__utma': '57812459.809408900.1680438933.1680438937.1680438937.1',
            '__utmc': '57812459',
            '__utmz': '57812459.1680438937.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
            '_hjSessionUser_1195751': 'eyJpZCI6ImFjYTgwOTY1LWY0NjUtNWIxOS1iNmJiLTdiY2U1ZWJjZGUzYiIsImNyZWF0ZWQiOjE2ODA0Mzg5MzQzOTksImV4aXN0aW5nIjp0cnVlfQ==',
            'vscommerce': 'c78am3e46ecm554ic2ppmngtm5',
            '_gat_gtag_UA_180928363_1': '1',
            '_hjIncludedInSessionSample_1195751': '0',
            '__utmt': '1',
            'cookie_policy': 'accepted',
            'VSReferrer': 'https%3A%2F%2Fwww.prolifedistribution.co.uk%2Fregister',
            'vsaid.b98d': 'b7f7ff52-3907-417f-8611-96cdf37261ea.1680438933.1.1680440511.1680438933.8d4acc41-acb6-467b-ad49-0b40ff429c4f',
            '_ga_CFWD5GQ5G4': 'GS1.1.1680438933.1.1.1680440510.0.0.0',
            '__uzmcj3': '537002532233',
            '__uzmdj3': '1680440511',
            '_ga': 'GA1.3.809408900.1680438933',
            '__utmb': '57812459.12.9.1680440512251',
        }

        headers = {
            'authority': 'www.prolifedistribution.co.uk',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,fr;q=0.6',
            'cache-control': 'max-age=0',
            'cookie': 'VSCurrency=GBP; vsases.b98d=*; __ssds=3; _gid=GA1.3.1851888342.1680438934; _hjFirstSeen=1; _hjSession_1195751=eyJpZCI6IjliOGM0MTNhLWI3N2ItNGU2Ny1hY2YxLWEzZDg2ZDc0MDQyNyIsImNyZWF0ZWQiOjE2ODA0Mzg5MzQ0MTIsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=1; __ssuzjsr3=a9be0cd8e; __uzmaj3=088f78ca-6239-41af-84f0-28faccdbbf4d; __uzmbj3=1680438934; __utma=57812459.809408900.1680438933.1680438937.1680438937.1; __utmc=57812459; __utmz=57812459.1680438937.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _hjSessionUser_1195751=eyJpZCI6ImFjYTgwOTY1LWY0NjUtNWIxOS1iNmJiLTdiY2U1ZWJjZGUzYiIsImNyZWF0ZWQiOjE2ODA0Mzg5MzQzOTksImV4aXN0aW5nIjp0cnVlfQ==; vscommerce=c78am3e46ecm554ic2ppmngtm5; _gat_gtag_UA_180928363_1=1; _hjIncludedInSessionSample_1195751=0; __utmt=1; cookie_policy=accepted; VSReferrer=https%3A%2F%2Fwww.prolifedistribution.co.uk%2Fregister; vsaid.b98d=b7f7ff52-3907-417f-8611-96cdf37261ea.1680438933.1.1680440511.1680438933.8d4acc41-acb6-467b-ad49-0b40ff429c4f; _ga_CFWD5GQ5G4=GS1.1.1680438933.1.1.1680440510.0.0.0; __uzmcj3=537002532233; __uzmdj3=1680440511; _ga=GA1.3.809408900.1680438933; __utmb=57812459.12.9.1680440512251',
            'referer': 'https://www.prolifedistribution.co.uk/register',
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

        params = {
            # 'cache': 'false',
        }

        content = requests.get(url, params=params, cookies=cookies, headers=headers)

        soup = BeautifulSoup(content.text, 'html.parser')
        prod = soup.find_all("tr", {"class": "filter-attribute-table-row"})
        # print(prod, end='\n\n\n')
        # filter-attribute-table-row
        try:
            product_description = soup.find("div", {"class": "product-tabs__content__cms"}).get_text()
        except:
            product_description = ''
        # print(product_description, end='\n\n\n')
        try:
            product_images = soup.find("a", {"class": "product__image__zoom-link"})["href"]
        except:
            product_images = ''
        # for image in product_images:
        #     print(image["href"])
        # print(product_images)
        # print('\n\n\n')
        # print(' '.join(product_images))
        for p in prod:
            # print(url)

            data = {
                'Collection Name': '',
                'Product Title': '',
                'Product Images Link': '',
                'Product Price': '',
                'Discounted Price': '',
                'Product Description': '',
            }

            try:
                product_collection = soup.find("span", {"class": "product-content__title--brand product-content__title--brand-offer"}).find_all(string=True, recursive=False)[-1]
            except:
                product_collection = ''

            # product_collection = p.find("span", {"class": "product-price-breaks-table__product-name"}).find("span").find("span").find_all(string=True, recursive=False)[-1]
            try:
                product_name = p.find("span", {"class": "product-price-breaks-table__product-name"}).find("span").find_all(string=True, recursive=False)[-1]
            except:
                product_name = ''
            try:
                product_retail_price = p.find("span", {"class": "product-content__price--ex"}).find("span").find_all(string=True, recursive=False)[-1]
            except:
                product_retail_price = ''
            try:
                product_discount_price = p.find("span", {"class": "product__details__prices__price--sale"}).find("span", {"class": "product-content__price--ex"}).find("span").find_all(string=True, recursive=False)[-1]
                product_retail_price = p.find("span", {"class": "product__details__prices__rrp"}).find("span", {"class": "product-content__price--ex"}).find("span").find_all(string=True, recursive=False)[-1]
            except:
                product_discount_price = ''
            # print(product_collection + ' +++ ' + product_name + ' +++ ' + product_discount_price + ' +++ ' + product_retail_price )
            # print(product_discount_price)

            try:
                data['Collection Name'] = product_collection
            except:
                data['Collection Name'] = ''

            try:
                data['Product Title'] = product_name
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
                data['Product Images Link'] = product_images
            except:
                data['Product Images Link'] = ''

            try:
                data['Product Description'] = product_description
            except:
                data['Product Description'] = ''

            writer.writerow(data)
            print(url)
            print('ok')

        # print(product_name)
        # print(url)



csvfile.close()













































































































































# import requests
#
# cookies = {
#     'VSCurrency': 'GBP',
#     'vsases.b98d': '*',
#     '__ssds': '3',
#     '_gid': 'GA1.3.1851888342.1680438934',
#     '_gat_gtag_UA_180928363_1': '1',
#     '_hjFirstSeen': '1',
#     '_hjIncludedInSessionSample_1195751': '0',
#     '_hjSession_1195751': 'eyJpZCI6IjliOGM0MTNhLWI3N2ItNGU2Ny1hY2YxLWEzZDg2ZDc0MDQyNyIsImNyZWF0ZWQiOjE2ODA0Mzg5MzQ0MTIsImluU2FtcGxlIjpmYWxzZX0=',
#     '_hjAbsoluteSessionInProgress': '1',
#     '__ssuzjsr3': 'a9be0cd8e',
#     '__uzmaj3': '088f78ca-6239-41af-84f0-28faccdbbf4d',
#     '__uzmbj3': '1680438934',
#     '__utma': '57812459.809408900.1680438933.1680438937.1680438937.1',
#     '__utmc': '57812459',
#     '__utmz': '57812459.1680438937.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
#     '__utmt': '1',
#     '_hjSessionUser_1195751': 'eyJpZCI6ImFjYTgwOTY1LWY0NjUtNWIxOS1iNmJiLTdiY2U1ZWJjZGUzYiIsImNyZWF0ZWQiOjE2ODA0Mzg5MzQzOTksImV4aXN0aW5nIjp0cnVlfQ==',
#     'vscommerce': 'c78am3e46ecm554ic2ppmngtm5',
#     '_ga_CFWD5GQ5G4': 'GS1.1.1680438933.1.1.1680438964.0.0.0',
#     '_ga': 'GA1.3.809408900.1680438933',
#     '__uzmcj3': '216691626543',
#     '__uzmdj3': '1680438965',
#     '__utmb': '57812459.6.9.1680438965684',
#     'vsaid.b98d': 'b7f7ff52-3907-417f-8611-96cdf37261ea.1680438933.1.1680438975.1680438933.8d4acc41-acb6-467b-ad49-0b40ff429c4f',
# }
#
# headers = {
#     'authority': 'www.prolifedistribution.co.uk',
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,fr;q=0.6',
#     'cache-control': 'max-age=0',
#     # 'cookie': 'VSCurrency=GBP; vsases.b98d=*; __ssds=3; _gid=GA1.3.1851888342.1680438934; _gat_gtag_UA_180928363_1=1; _hjFirstSeen=1; _hjIncludedInSessionSample_1195751=0; _hjSession_1195751=eyJpZCI6IjliOGM0MTNhLWI3N2ItNGU2Ny1hY2YxLWEzZDg2ZDc0MDQyNyIsImNyZWF0ZWQiOjE2ODA0Mzg5MzQ0MTIsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=1; __ssuzjsr3=a9be0cd8e; __uzmaj3=088f78ca-6239-41af-84f0-28faccdbbf4d; __uzmbj3=1680438934; __utma=57812459.809408900.1680438933.1680438937.1680438937.1; __utmc=57812459; __utmz=57812459.1680438937.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; _hjSessionUser_1195751=eyJpZCI6ImFjYTgwOTY1LWY0NjUtNWIxOS1iNmJiLTdiY2U1ZWJjZGUzYiIsImNyZWF0ZWQiOjE2ODA0Mzg5MzQzOTksImV4aXN0aW5nIjp0cnVlfQ==; vscommerce=c78am3e46ecm554ic2ppmngtm5; _ga_CFWD5GQ5G4=GS1.1.1680438933.1.1.1680438964.0.0.0; _ga=GA1.3.809408900.1680438933; __uzmcj3=216691626543; __uzmdj3=1680438965; __utmb=57812459.6.9.1680438965684; vsaid.b98d=b7f7ff52-3907-417f-8611-96cdf37261ea.1680438933.1.1680438975.1680438933.8d4acc41-acb6-467b-ad49-0b40ff429c4f',
#     'referer': 'https://www.prolifedistribution.co.uk/register',
#     'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
#     'sec-ch-ua-mobile': '?1',
#     'sec-ch-ua-platform': '"Android"',
#     'sec-fetch-dest': 'document',
#     'sec-fetch-mode': 'navigate',
#     'sec-fetch-site': 'same-origin',
#     'sec-fetch-user': '?1',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36',
# }
#
# params = {
#     'cache': 'false',
# }
#
# response = requests.get('https://www.prolifedistribution.co.uk/customer', params=params, cookies=cookies, headers=headers)