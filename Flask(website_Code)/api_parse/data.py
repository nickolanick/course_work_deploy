from bs4 import BeautifulSoup
import urllib.request


def get_html_content(name_of_product):
    """ str -> BeautifulSoap """
    url = "https://rozetka.com.ua/ua/search/?text=" + name_of_product
    with urllib.request.urlopen(url) as response:
        html = response.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        new_url = soup.find("div", class_="g-i-tile-i-box-desc").find("a")[
                      "href"] + "/comments/sort=helpful/"
        data = map(lambda x: x.text, get_comments(new_url))

        return data


def get_comments(url):
    """ str -> str """
    with urllib.request.urlopen(url) as response:
        soup = BeautifulSoup(response.read().decode("utf-8"), "html.parser")

        info_comments = (
            soup.find_all("div", "pp-review-inner"))
        # for elem in range(len(info_comments)):
        #     for g in range(3):
        #         pass
        return soup.find_all("div", "pp-review-text-i")


if __name__ == '__main__':
    for i in get_html_content(input(
            "enter name of product to EXPLORE! for example iphone 6, macbook air, etc... : ")):
        print(i)
