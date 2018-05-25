# File: hotline_parser.py
# Module has functionality that allow parse comments from hot line.
from .comment import Comment
import urllib.request
from bs4 import BeautifulSoup


def insert_comments_2(container, name_of_product):
    """ Add parsed comments to container. """
    try:
        url = "https://hotline.ua/sr/?q=" + name_of_product.replace(" ", "+")
        with urllib.request.urlopen(url) as response:
            html = response.read().decode("utf-8")
            soup = BeautifulSoup(html, "html.parser")
            url = "https://hotline.ua" + \
                soup.find("div", class_="info-description").find("a")["href"]
        with urllib.request.urlopen(url) as response:
            html = response.read().decode("utf-8")
            soup = BeautifulSoup(html, "html.parser")
            new_url = soup.find("div", class_="text")
            if new_url is not None:
                new_url = new_url.text.strip()
        get_comments(container, url)
        return new_url
    except AttributeError:
        pass


def get_comments(container, url):
    """ Return description and comments. """
    with urllib.request.urlopen(url + "/discussion") as response:
        html = response.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        mark = soup.find("div", class_="value-rating")
        if mark is not None:
            mark = float(mark.text)
        for com in soup.find_all("div", class_="review-item row"):
            com = com.find_all("div", class_="text")
            text = ""
            for i in range(len(com)):
                if i == 0:
                    text += com[i].text.strip().replace("\n", " ")
                else:
                    text += "\n" + com[i].text.strip()
            if text:
                container.comments.append(Comment(text, mark))
