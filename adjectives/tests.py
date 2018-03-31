words_container = AdjectivesContainer()

comment1 = CommentImplemented(
    "злий злий злий собака злий добрий добрий смішний веселий",
    9, 9)
comment2 = CommentImplemented(
    "добрий злий злий злий поганий поганий",
    2, 9)
adj_cont = AdjectivesContainerImplemented()
cm = CommentsImplemented(adj_cont)
cm.add_comments([comment1, comment2])
cm.process_new_comments()
adj_cont.process_all_adjectives()
print(adj_cont.positive_adjectives)
print(adj_cont.negative_adjectives)
