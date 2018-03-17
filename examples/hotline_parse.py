from bs4 import BeautifulSoup
import urllib.request

"""
https://hotline.ua/sr/?q=
"""


def hot_line(name_of_product):
    url = "https://hotline.ua/sr/?q=" + name_of_product.replace(" ", "+")
    with urllib.request.urlopen(url) as response:
        html = response.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        new_url = "https://hotline.ua/" + soup.find("div", class_="info-description").find("a")["href"]

        # data = map(lambda x: x.text, get_comments(new_url))
        return find_inf(new_url[0:-1])
        # return data


def find_inf(url):
    print(url[0:-1], "URL")
    with urllib.request.urlopen(url) as response:
        html = response.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        new_url = soup.find("div", class_="text")
        return str(new_url.text)
