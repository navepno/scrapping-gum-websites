import requests
from bs4 import BeautifulSoup
import csv
import openpyxl
import re

url = "https://www.powerbody.eu/manufacturer/manufacturer/index/"
headers = {
    'User-Agent': 'My User Agent 1.0',
    'From': 'youremail@domain.example'  # This is another valid field
}
content = requests.get(url, headers=headers)

soup = BeautifulSoup(content.text, 'html.parser')

fieldnames = ['Product Title', 'Product Additional Title', 'Product Images Link', 'Product Price', 'Discounted Price', 'Collection Name',
              'Tags', 'Product Description']




# brands-list
list_brand = []
list_product = []
folder_brand = soup.find_all("div", {"class": "brands-list"})
for i in range(len(folder_brand)):
    # print(i)
    for link in folder_brand[i].find_all("a"):
        try:
            list_brand.append(link['href']+'?limit=all&p')
        except:
            pass
# for b in folder_brand:
#     brands = b.find_all("a")
#     for brand in brands:
#         link = brand['href']
#         list_brand.append(link)

# print(list_brand[0])


# working with brand
# for link in list_brand:
#     headers = {
#         'User-Agent': 'My User Agent 1.0',
#         'From': 'youremail@domain.example'  # This is another valid field
#     }
#     content = requests.get(link, headers=headers)
#
#     soup = BeautifulSoup(content.text, 'html.parser')
#     # print(soup)


test11 = 1
# get link of product
# print(folder_brand[1].find_all("a")[1]['href'])
for link in list_brand:
    content = requests.get(link, headers=headers)

    soup = BeautifulSoup(content.text, 'html.parser')
    product_list = soup.find_all("a", {"class": "product-info-top__product-name"})
    for product in product_list:
        list_product.append(product['href'])
        print('prod ok', product['href'])

# working with product
test = list_product[0]






cookies = {
    'frontend_cid': 'hnbHKPYy3KHLS6Ni',
    '_gcl_au': '1.1.241118049.1680343177',
    'external_no_cache': '1',
    'show_cookie_pb': '1',
    'smuuid': '1873c42169e-ac9a021329ff-f4c131f2-86c39288-ce7a4c41-e34a92b3e829',
    '_ga': 'GA1.3.1912986771.1680343177',
    '_gid': 'GA1.3.1878573003.1680343177',
    '_smvs': 'DIRECT',
    '_hjFirstSeen': '1',
    '_hjIncludedInSessionSample_1132165': '0',
    '_hjSession_1132165': 'eyJpZCI6ImZiY2E0MGY0LWM2MDItNDdlYS1hOGY0LTMxYTM4ZGJiMTA1ZiIsImNyZWF0ZWQiOjE2ODAzNDMxNzcyNjgsImluU2FtcGxlIjpmYWxzZX0=',
    '_hjAbsoluteSessionInProgress': '0',
    '_hjShownFeedbackMessage': 'true',
    '_hjSessionUser_1132165': 'eyJpZCI6ImY3OTY3NjI4LTZmMmYtNWM3Zi1iNjU3LTc2YWYyM2M0NWY2MSIsImNyZWF0ZWQiOjE2ODAzNDMxNzcyMzUsImV4aXN0aW5nIjp0cnVlfQ==',
    'frontend': '90vafo04of6he86ku8k7cg2llm',
    'smcntctgs': 'strvw%2Cnws',
    'smclient': 'b72d1d3e-5c31-41ba-af8f-d1400ddd4df8',
    'smvr': 'eyJ2aXNpdHMiOjEsInZpZXdzIjo0LCJ0cyI6MTY4MDM0MzIyMzg2MSwibnVtYmVyT2ZSZWplY3Rpb25CdXR0b25DbGljayI6MCwiaXNOZXdTZXNzaW9uIjpmYWxzZX0=',
    'last_visit_time': '1680343224',
}

headers = {
    'authority': 'www.powerbody.eu',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,fr;q=0.6',
    'cache-control': 'max-age=0',
    # 'cookie': 'frontend_cid=hnbHKPYy3KHLS6Ni; _gcl_au=1.1.241118049.1680343177; external_no_cache=1; show_cookie_pb=1; smuuid=1873c42169e-ac9a021329ff-f4c131f2-86c39288-ce7a4c41-e34a92b3e829; _ga=GA1.3.1912986771.1680343177; _gid=GA1.3.1878573003.1680343177; _smvs=DIRECT; _hjFirstSeen=1; _hjIncludedInSessionSample_1132165=0; _hjSession_1132165=eyJpZCI6ImZiY2E0MGY0LWM2MDItNDdlYS1hOGY0LTMxYTM4ZGJiMTA1ZiIsImNyZWF0ZWQiOjE2ODAzNDMxNzcyNjgsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _hjShownFeedbackMessage=true; _hjSessionUser_1132165=eyJpZCI6ImY3OTY3NjI4LTZmMmYtNWM3Zi1iNjU3LTc2YWYyM2M0NWY2MSIsImNyZWF0ZWQiOjE2ODAzNDMxNzcyMzUsImV4aXN0aW5nIjp0cnVlfQ==; frontend=90vafo04of6he86ku8k7cg2llm; smcntctgs=strvw%2Cnws; smclient=b72d1d3e-5c31-41ba-af8f-d1400ddd4df8; smvr=eyJ2aXNpdHMiOjEsInZpZXdzIjo0LCJ0cyI6MTY4MDM0MzIyMzg2MSwibnVtYmVyT2ZSZWplY3Rpb25CdXR0b25DbGljayI6MCwiaXNOZXdTZXNzaW9uIjpmYWxzZX0=; last_visit_time=1680343224',
    'referer': 'https://www.powerbody.eu/customer/account/login/',
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

csvfile = open(f'/Users/navepno/prod/gumstuffscrapping/first.csv', 'w', newline='')
writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
writer.writeheader()

for prod in list_product:
    try:
        data = {
            'Product Title': '',
            'Product Additional Title': '',
            'Product Images Link': '',
            'Product Price': '',
            'Discounted Price': '',
            'Collection Name': '',
            'Tags': '',
            'Product Description': '',
        }
        content = requests.get(prod, cookies=cookies, headers=headers)
        product_soup = BeautifulSoup(content.text, 'html.parser')

        product_options = product_soup.find_all("div", {"class": "product-option-group"})
        product_image = product_soup.find("img", {"class": "elevate-image"})['src']
        product_additional_name = product_soup.find("span", {"class": "additional_name"}).string
        product_collection = product_soup.find("span", {"class": "product-header__product-name"}).string
        # product_description = product_soup.find("div", {"class": "product-description"}).find("p").string
        try:
            product_description = product_soup.find("div", {"class": "product-description__content content-description"}).find("p").find_all(
                string=True, recursive=False)[0]
        except:
            product_description = product_soup.find("div", {"class": "product-description__content"}).find_all(
                string=True, recursive=False)
            product_description = ' '.join(product_description[1:])
            # print(product_description)
        # not a comment
        for product_option in product_options:
            product_title = product_option.find_all("div", {"class": "label_information"})
            product_name = product_option.find("div", {"class": "label_information"}).find_all(string=True, recursive=False)[0][1:]
            product_retail_price = product_option.find("div", {"class": "price-retail fright"}).find("div", {"class": "price"}).string
            product_discounted_price = product_option.find("div", {"class": "your-price fright"}).find("div", {"class": "price"}).find_all(string=True, recursive=False)[0][1:]
            # print(product_discounted_price)
            # price-save
            # print(product_name)
            try:
                product_ean = product_title[0].find("p", {"class": "product-ean-info"}).string.split(':')[1][1:]
            except:
                product_ean = ''
            # print(product_title[0])
            # print('\n\n\n\n')
            # print(product_description)

            data['Product Title'] = product_additional_name
            data['Product Additional Title'] = product_name
            data['Product Images Link'] = product_image
            data['Product Price'] = product_retail_price
            data['Discounted Price'] = product_discounted_price
            data['Collection Name'] = product_collection
            data['Tags'] = product_ean
            data['Product Description'] = product_description

            writer.writerow(data)
            # print(f'{product_name}---{product_ean}---{product_image}---{product_retail_price}---{product_collection}---{product_description}')
    except:
        print('!!!!!!')
        print(prod)
        print('!!!!!!')



csvfile.close()






# print(product_options[0])

# print('1231231-3213-12-3-1-31-3-12-3-1-31-')
# print(div_tag)

# print(product_options[0])








# headers = {
#     'User-Agent': 'My User Agent 1.0',
#     'From': 'youremail@domain.example'  # This is another valid field
# }
# content = requests.get(test, headers=headers)
#
# product_soup = BeautifulSoup(content.text, 'html.parser')
# product_name =
# print(response)