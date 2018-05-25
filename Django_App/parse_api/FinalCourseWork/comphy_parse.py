# File: comphy_parse.py
# Module has functionality that allow parse comments from Comphy web shop.
from .comment import Comment
from bs4 import BeautifulSoup
import requests


def insert_comments_3(container, name_of_product):
    """ Add parsed comments to the container. """
    try:
        url = "https://comfy.ua/ua/catalogsearch/result?q=" + name_of_product
        html = requests.get(url)
        soup = BeautifulSoup(html.text, "html.parser")
        new_url = soup.find("div", "js-products-list-wrap"
                            ).find("div", "products-list")
        new_url = new_url.find("div", "product-item").get("data-product-url")
        if new_url is not None:
            new_url = create_comment_url(new_url)
            soup = BeautifulSoup(requests.get(new_url).text, "html.parser")
            process_container(container, soup)
    except AttributeError:
        pass


def create_comment_url(url):
    """ Create a new url with comments. """
    review = "-otzyvy"
    return url[0:-5] + review + url[-5:]


def process_container(container, soup):
    """ Add comments to container. """
    mark = soup.find("span", "feedback-info__label")
    if mark is not None:
        mark = mark.text.strip()
        if mark != "" and mark[0].isdigit():
            mark = int(mark[0])
        else:
            mark = None
    comments = soup.find_all("li", "feedback-item")
    if comments is not None:
        for comment in comments:
            messages = comment.find_all("p", "feedback-item__msg")
            if messages is not None:
                text = ""
                for message in messages:
                    text += message.text.strip() + "\n"
                container.comments.append(Comment(text, mark))
