# File: comment.py
# Module has a Comment and Comments classes.


class Comment:
    """ Represents a comment object. """
    def __init__(self, text, mark=None):
        """ Initialize a text of comment and mark. """
        self.text = text
        self.mark = mark


class Comments:
    """ Represent a conatainer of comments. """
    def __init__(self):
        """ Initialize an empty list. """
        self.comments = []
        self.average_mark = None

    def determine_average_mark(self):
        """ Initialize an average mark among all comments. """
        total, divide = 0, 0
        for comment in self.comments:
            if comment.mark is not None:
                total += comment.mark
                divide += 1
        if divide == 0:
            divide = 1
        return total // divide
