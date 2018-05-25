import urllib.request
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

req = Request(
    'http://www.google.com/search?q=cake&tbm=isch',
    headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req)
html = webpage.read().decode("utf-8")
print(html)
# soup = BeautifulSoup(html, "html.parser")
# print(soup.find("img"))
# def parse_img(name_product):
#     url = "https://www.google.com/search?tbm=isch&source=hp&biw=1680&bih=953&ei=9cQCW_rpCIOusAHIr5XoBw&q={}+hd".format(
#         name_product)
#     print(url)
#     with urllib.request.urlopen(url) as response:
#         html = response.read().decode("utf-8")
#         soup = BeautifulSoup(html, "html.parser")
#         print(soup)
#         # new_url = "https://hotline.ua/" + \
#         #           soup.find("div", class_="info-description").find("img")
#         # print(new_url)
#         # return find_inf(new_url[0:-1])
# parse_img("Iphone+7")
