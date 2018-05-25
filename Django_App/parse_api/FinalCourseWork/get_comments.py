# File: get_comments.py
# Module has a function that return comments from three websites, description
# of product and average mark.
from .rozetka_parse import insert_comments_1
from .hotline_parse import insert_comments_2
from .comphy_parse import insert_comments_3
from .comment import Comments
import time


def get_description(name_of_product):
    comments = Comments()
    # insert_comments_1(comments, name_of_product)
    description = insert_comments_2(comments, name_of_product)
    # insert_comments_3(comments, name_of_product)
    final_comment = ""
    for com in comments.comments:
        final_comment += com.text.strip() + "~"
    return final_comment, description, comments.determine_average_mark()


def get_comments_other(name_of_product):
    """
    str -> tuple

    Return comments, description and average mark.
    """

    comments = Comments()
    insert_comments_1(comments, name_of_product)
    insert_comments_3(comments, name_of_product)
    final_comment = ""
    for com in comments.comments:
        final_comment += com.text.strip()+"~"
    return final_comment, comments.determine_average_mark()
