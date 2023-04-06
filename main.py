# Import modules
import turtle
import random
import math
import statistics
import os


# Language Processing Code

def check_if_identical(text1, text2):
    if text1 == text2:
        return True
    else:
        return False


def checks_if_similar_wordchice(text1, text2):
    similarWords = set()
    similarWordChoice = False

    UniqueWordsText1 = len(set(list(text1)))
    UniqueWordsText2 = len(set(list(text2)))

    for word in text1:
        if word in text2:
            set.add(word)

    if len(similarWords) > 0.8 * (statistics.mean(UniqueWordsText1, UniqueWordsText2)):
        similarWordChoice = True

    return similarWordChoice


def jaccard_similarity(x, y):
    # returns the jaccard similarity between two lists

    intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
    union_cardinality = len(set.union(*[set(x), set(y)]))

    return intersection_cardinality / float(union_cardinality)


def compare_similarity(text1, text2):
    similarity_score = 0
    similarWordChoice = False

    # checks if they are identical
    if check_if_identical(text1, text2):
        similarity_score = 1
        return {"SimilarityScore": similarity_score, "SimilarWordChoice": similarWordChoice}

    # if checks_if_similar_wordchice(text1, text2):
    # similarWordChoice = True

    return {"SimilarityScore": jaccard_similarity(text1, text2), "SimilarWordChoice": similarWordChoice}


def isSentencePlagarized(sentence, text2):
    wordChoice = False
    similarScore = 0

    similarScore_local = []
    wordChoice_local = []
    for i in text2:
        similarScore_local.append(compare_similarity(sentence, text2)["SimilarityScore"])
        similarScore_local.append(compare_similarity(sentence, text2)["SimilarWordChoice"])
    if True in wordChoice_local:
        wordChoice = True
    else:
        wordChoice = False

    similarScore.append(max(similarScore_local))

    if (wordChoice == True) and similarScore > 0.75:
        return True
    else:
        return False

    # Ask User Turtle Logic


def askUserWhoSuspectIs(pen, files):
    pen.goto(-300, 300)
    pen.write("Which file do you suspect of plagarism?", font=("Verdana",
                                                               15, "normal"))

    pen.goto(-200, 300)

    pen.setheading(270)

    for i in files:
        pen.forward(30)
        pen.write(f" {files.index(i) + 1}: {i}", font=("Verdana", 11, "normal"))

    suspect_num = int(turtle.textinput("Who you you suspect?", "Suspect #"))
    return suspect_num - 1


def articlePlagarized(suspect_num, data):
    pass


if __name__ == "__main__":
    # All GUI Logic
    wn = turtle.Screen()
    wn.bgcolor("beige")

    files = os.listdir("Data")

    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.up()

    suspect_num = askUserWhoSuspectIs(pen, files)

    articlePlagarized(suspect_num, files)

    wn.mainloop()
