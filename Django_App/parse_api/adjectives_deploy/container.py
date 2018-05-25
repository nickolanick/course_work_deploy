from main import AdjectivesContainer


class Container(AdjectivesContainer):

    @staticmethod
    def add_adjective(adjective, adjectives, length):
        start = 0
        end = length - 1
        while start <= end:
            i = (start + end) // 2
            if adjectives[i][0] == adjective:
                adjectives[i][1] += 1
                return True
            elif adjectives[i][0] > adjective:
                end = i - 1
            else:
                start = i + 1
        else:
            adjectives.insert(start, [adjective, 1])
        return False

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
            if not Container.add_adjective(positive, self.positive_adjectives,
                                           length):
                length += 1

    def process_negative_adjectives(self, negatives):
        length = len(self.negative_adjectives)
        for negative in negatives:
            if not Container.add_adjective(negative, self.negative_adjectives,
                                           length):
                length += 1


# container = Container()
# container.process_negative_adjectives(["c", "b", "a", "z", "l"])
# container.process_positive_adjectives(["c", "b", "a", "z", "l"])
# print("neg - ", container.negative_adjectives)
# print("pos - ", container.positive_adjectives)
# container.process_all_adjectives()
# print("neg - ", container.negative_adjectives)
# print("pos - ", container.positive_adjectives)
