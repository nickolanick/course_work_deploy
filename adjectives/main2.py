import copy
from string import punctuation

from adjectives.main1 import AdjectivesContainer, Comment, Comments

punctuation += " "


class CommentImplemented(Comment):
    """ Represents a comment object. """

    def parse_adjectives(self):
        """ object -> list """
        result, current = [], ""
        for letter in self.text:
            if letter not in punctuation:
                current += letter
            else:
                if current.endswith("ий") or current.endswith("ій"):
                    result.append(current)
                elif current.endswith("ая"):
                    result.append(current[:-2] + "ий")
                elif current.endswith("яя"):
                    result.append(current[:-2] + "ій")
                elif current.endswith("е"):
                    result.append(current[:-1] + "ий")
                current = ""
        return result

    def parse_positive_adjectives(self):
        """ object -> list """
        if self.comment_characteristic < 8:
            raise TypeError
        return self.parse_adjectives()

    def parse_negative_adjectives(self):
        """ object -> list """
        if self.comment_characteristic > 3:
            raise TypeError
        return self.parse_adjectives()

    def define_comment_characteristic(self, positives, negatives):
        """ list(list) -> None """
        current = 0
        adjectives = self.parse_adjectives()
        for word in positives:
            if word[0] in adjectives:
                current += word[1]
        for word in negatives:
            if word[0] in adjectives:
                current -= word[1]
        if current > 10:
            self.comment_characteristic = 10
        elif current < -10:
            self.comment_characteristic = 0
        else:
            self.comment_characteristic = (10 - current % 10) % 10


class CommentsImplemented(Comments):
    """ Represnt comments object. """

    def add_comments(self, comments):
        """ list -> None """
        if isinstance(comments, list):
            self.comments.extend(comments)
        else:
            self.comments.append(comments)

    def process_new_comments(self):
        """ None -> None """
        length = len(self.comments)
        for i in range(self.pointer, length):
            if self.comments[i].comment_characteristic > 7:
                for element in self.comments[i].parse_positive_adjectives():
                    if element in self.adjective_container.positive_adjectives.keys():
                        self.adjective_container.positive_adjectives[
                            element] += 1
                    else:
                        self.adjective_container.positive_adjectives[
                            element] = 1
            elif self.comments[i].comment_characteristic < 4 and self.comments[
                i].comment_characteristic > 0:
                for element in self.comments[i].parse_negative_adjectives():
                    if element in self.adjective_container.negative_adjectives.keys():
                        self.adjective_container.negative_adjectives[
                            element] += 1
                    else:
                        self.adjective_container.negative_adjectives[
                            element] = 1
        self.pointer = length


class AdjectivesContainerImplemented(AdjectivesContainer):
    """ Represents adjectives container object. """

    def process_all_adjectives(self):
        """ None -> None """

        temp_possitve = copy.deepcopy(self.positive_adjectives)
        for good_word in temp_possitve:
            if good_word in self.negative_adjectives:
                if self.negative_adjectives[good_word] >= \
                        self.positive_adjectives[good_word]:

                    self.positive_adjectives[good_word] += \
                        self.negative_adjectives[good_word]
                    del self.negative_adjectives[good_word]
                else:
                    self.negative_adjectives[good_word] += \
                        self.positive_adjectives[good_word]
                    del self.positive_adjectives[good_word]
