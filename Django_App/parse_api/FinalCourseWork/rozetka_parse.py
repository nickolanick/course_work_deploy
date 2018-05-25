# File: rozetka_parse.py
# Module has a functionality that allow take comments from rozetka web shop.
from bs4 import BeautifulSoup
import urllib.request
from .comment import Comment


def insert_comments_1(container, name_of_product):
    """ Create comments from rozetka web shop and add them to container. """
    url = "https://rozetka.com.ua/ua/search/?text=" + name_of_product
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read().decode("utf-8")
            soup = BeautifulSoup(html, "html.parser")
            new_url = soup.find("div", class_="g-i-tile-i-box-desc").find("a")[
                      "href"] + "/comments/sort=helpful/"
            for com in get_comments(new_url):
                mark = com.find("span", "sprite g-rating-stars-i")
                if mark is not None:
                    mark = int(mark.get("content"))
                content, text = com.findAll("div", "pp-review-text-i"), ""
                for i in range(len(content)):
                    text += content[i].text.strip() + "\n"
                text = text.strip()
                if text[-1] != "?":
                    container.comments.append(Comment(text, mark))
    except AttributeError:
        pass


def get_comments(url):
    """ str -> str """
    with urllib.request.urlopen(url) as response:
        soup = BeautifulSoup(response.read().decode("utf-8"), "html.parser")

        comments = soup.find_all("div", "pp-review-inner")
        return comments
