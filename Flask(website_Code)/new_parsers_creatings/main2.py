from string import punctuation

from main import AdjectivesContainer, Comment, Comments

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
                self.adjective_container.process_positive_adjectives(
                    self.comments[i].parse_positive_adjectives())
            elif self.comments[i].comment_characteristic < 3:
                self.adjective_container.process_negative_adjectives(
                    self.comments[i].parse_negative_adjectives())
        self.pointer = length

    def evaluate(self):
        length1 = len(self.adjective_container.positive_adjectives)
        length2 = len(self.adjective_container.negative_adjectives)
        for comment in self.comments:
            if comment.comment_characteristic == 0:
                current = 0
                for adjective in comment.parse_adjectives():
                    if isinstance(AdjectivesContainerImplemented.add_adjective(adjective,
                                self.adjective_container.positive_adjectives, length1,
                                False), bool):
                        current += 1
                    if isinstance(AdjectivesContainerImplemented.add_adjective(adjective,
                                self.adjective_container.negative_adjectives, length2,
                                False), bool):
                        current -= 1
                print(current)
                if current > 6:
                    comment.comment_characteristic = 10
                elif current < 0:
                    comment.comment_characteristic = 1
                else:
                    comment.comment_characteristic = (2 * current) % 10


class AdjectivesContainerImplemented(AdjectivesContainer):
    """ Represents adjectives container object. """

    @staticmethod
    def add_adjective(adjective, adjectives, length, status=True):
        start = 0
        end = length - 1
        while start <= end:
            i = (start + end) // 2
            if adjectives[i][0] == adjective:
                if status:
                    adjectives[i][1] += 1
                return True
            elif adjectives[i][0] > adjective:
                end = i - 1
            else:
                start = i + 1
        else:
            return start

    def process_all_adjectives(self):
        for i in range(len(self.negative_adjectives) - 1, -1, -1):
            for positive in self.positive_adjectives:
                if self.negative_adjectives[i][0] == positive[0]:
                    if self.negative_adjectives[i][1] > positive[1]:
                        self.positive_adjectives.remove(positive)
                    elif positive[1] > self.negative_adjectives[i][1]:
                        self.negative_adjectives.remove(
                            self.negative_adjectives[i])
                    else:
                        self.positive_adjectives.remove(positive)
                        self.negative_adjectives.remove(
                            self.negative_adjectives[i])
                    break

    def process_positive_adjectives(self, positives):
        length = len(self.positive_adjectives)
        for positive in positives:
            current = AdjectivesContainerImplemented.add_adjective(positive,
                                                                   self.positive_adjectives,
                                                                   length)
            if current != True:
                self.positive_adjectives.insert(current, [positive, 1])
                length += 1

    def process_negative_adjectives(self, negatives):
        length = len(self.negative_adjectives)
        for negative in negatives:
            current = AdjectivesContainerImplemented.add_adjective(negative,
                                                                   self.negative_adjectives,
                                                                   length)
            if current != True:
                self.negative_adjectives.insert(current, [negative, 1])
                length += 1


c1 = CommentImplemented("дуже класний.", 10)
c2 = CommentImplemented("дуже поганий.", 2)
c3 = CommentImplemented("задоволений.", 9)
coms = CommentsImplemented(AdjectivesContainerImplemented())
coms.add_comments([c1, c2, c3])
coms.process_new_comments()
print(coms.adjective_container.positive_adjectives)
print(coms.adjective_container.negative_adjectives)
coms.adjective_container.process_all_adjectives()
print(coms.adjective_container.positive_adjectives)
print(coms.adjective_container.negative_adjectives)
c4 = CommentImplemented("хороший тул", 9)
c5 = CommentImplemented("поганий тел", 2)
coms.add_comments([c4, c5])
coms.process_new_comments()
print(coms.adjective_container.positive_adjectives)
print(coms.adjective_container.negative_adjectives)
coms.add_comments(c3)
coms.process_new_comments()
print(coms.adjective_container.positive_adjectives)
c5 = CommentImplemented("хороший задоволений.")
coms.add_comments(c5)
coms.evaluate()
print(coms.comments)
