class Comment:
    """ Represents an abstract class. """

    def __init__(self, text, comment_characteristic=0, constructive=0):
        """ Initialize three fields. """
        self.text = text
        self.comment_characteristic = comment_characteristic
        self.constructive = constructive

    def parse_positive_adjectives(self):
        """ Abstract method. """
        raise NotImplementedError("It is subclass responsibility.")

    def parse_negative_adjectives(self):
        """ Abstract method. """
        raise NotImplementedError("It is subclass responsibility.")

    def define_comment_characteristic(self, positives, negatives):
        """ Abstract method. """
        raise NotImplementedError("It is subclass responsibility.")

    def __str__(self):
        """ Srt method. """
        return "Comment:\nText: {}\nMark: {}\nConstructive:{}".format(
            self.text, self.comment_characteristic, self.constructive)

    def __repr__(self):
        return "text: {}, mark: {}, constructive:{}".format(
            self.text, self.comment_characteristic, self.constructive)

class Comments:
    """ Represents an abstract class. """

    def __init__(self, adjectives_container):
        """ Initialize three fields. """
        self.adjective_container = adjectives_container
        self.pointer = 0
        self.comments = []

    def add_comments(self, comments):
        """ Abstract method. """
        raise NotImplementedError("It is subclass responsibility.")

    def process_new_comments(self):
        """ Abstract method. """
        raise NotImplementedError("It is subclass responsibility.")


class AdjectivesContainer:
    """ Represents an abstract class. """

    def __init__(self):
        """ Initialize two empty lists. """
        self.positive_adjectives = []
        self.negative_adjectives = []

    def process_all_adjectives(self):
        """ Abstract method. """
        raise NotImplementedError("It is subclass responsibility.")

    def process_positive_adjectives(self, positives):
        """ Abstract method. """
        raise NotImplementedError("It is subclass responsibility.")

    def process_negative_adjectives(self, negatives):
        """ Abstract method. """
        raise NotImplementedError("It is subclass responsibility.")
