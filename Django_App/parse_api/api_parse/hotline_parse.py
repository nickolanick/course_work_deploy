import urllib.request

from bs4 import BeautifulSoup

from ..adjectives_deploy.abstract_classes_adjectives_Implementation_two import *

"""
https://hotline.ua/sr/?q=
"""


def hot_line(name_of_product):
    url = "https://hotline.ua/sr/?q=" + name_of_product.replace(" ", "+")
    with urllib.request.urlopen(url) as response:
        html = response.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        print(url)
        new_url = "https://hotline.ua/" + \
                  soup.find("div", class_="info-description").find("a")["href"]
        return find_inf(new_url[0:-1])


def find_inf(url):
    lst = []

    with urllib.request.urlopen(url) as response:
        html = response.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")

        new_url = soup.find("div", class_="text")

    description = str(new_url.text)
    with urllib.request.urlopen(url + "/discussion") as response:
        print(response)
        html = response.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        data = soup.find_all("div", class_="review-item row")
        data_ranked = soup.find_all("div", class_="rating")

        for i in range(len(data)):
            single_data = ""

            for elem in data[i].find("div", class_="row text").find_all("div",
                                                                        class_="cell-9 cell-sm"):
                single_data += elem.text.replace("\n", " ").strip()
            lst.append(CommentImplemented(single_data, int(float(
                data_ranked[i].find("div", class_="value-rating").text)) * 2,
                                          0))
    return description,lst

if __name__ == '__main__':
    for element in hot_line(input("enter mob: "))[1]:
        print(element)
