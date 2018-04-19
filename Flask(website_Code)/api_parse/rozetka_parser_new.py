from bs4 import BeautifulSoup
import urllib.request
from main2 import *


def define_rating(comment):
    """ str -> int """
    i = 0
    while comment[i].isdigit():
        i += 1
    return int(comment[:i])


def get_html_content(name_of_product):
    """ str -> BeautifulSoap """
    url = "https://rozetka.com.ua/ua/search/?text=" + name_of_product
    with urllib.request.urlopen(url) as response:
        html = response.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        new_url = soup.find("div", class_="g-i-tile-i-box-desc").find("a")[
                      "href"] + "/comments/sort=helpful/"
        comments = []
        for i in get_comments(new_url):
            text = ""
            content = i.findAll("div", "pp-review-text-i")
            length = len(content)
            for j in range(length):
                text += content[j].text.strip() + (
                    "\n" if j != length - 1 else "")
            try:
                rating = define_rating(i.find("div",
                                              "inline pp-comments-author-good"
                                              "-vote").text.strip())
            except:
                rating = 0
            try:
                mark = int(
                    i.find("span", "sprite g-rating-stars-i").get("content"))
            except:
                mark = 0
            comments.append(
                CommentImplemented(text, mark * 2, int(rating / 10)))
        return comments


def get_comments(url):
    """ str -> str """
    with urllib.request.urlopen(url) as response:
        soup = BeautifulSoup(response.read().decode("utf-8"), "html.parser")

        return soup.find_all("div", "pp-review-inner")


def analys_words(name):
    adj_cont = AdjectivesContainerImplemented()
    cm = CommentsImplemented(adj_cont)
    cm.process_new_comments()
    comments = get_html_content(name)
    for comment in comments:
        for sp in range(1, len(comment.text.split("\n"))):
            if "Недоліки:" in comment.text.split("\n")[sp] \
                    and "Переваги:" in comment.text.split("\n")[sp - 1]:
                possitive_one = CommentImplemented(
                    comment.text.split("\n")[sp - 1], 10, comment.constructive)

                negative = CommentImplemented(
                    comment.text.split("\n")[sp], 1, comment.constructive)
                regular = CommentImplemented(
                    comment.text.split("\n")[::sp],
                    comment.comment_characteristic, comment.constructive)
                cm.add_comments(possitive_one)
                cm.add_comments(negative)
                cm.add_comments(regular)
                print(comment.text.split("\n")[sp - 1], "POSSITTIVE")
                print(comment.text.split("\n")[sp], "NEGGATIVE")
                continue

        comm = CommentImplemented(
            comment.text,
            comment.comment_characteristic, comment.constructive)
        cm.add_comments(comm)
        print(comment.comment_characteristic)

    cm.process_new_comments()
    adj_cont.process_all_adjectives()
    print(adj_cont.positive_adjectives)
    print(adj_cont.negative_adjectives)


if __name__ == '__main__':
    analys_words(input(
        "enter name of product to EXPLORE! for example iphone 6, macbook air, etc... : "))
