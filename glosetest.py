#encoding: utf-8

from glosses import WordPair
from node import Node
from node import Queue

fil = open("swahiliu")
gloses = fil.read().split("\n")
queue = Queue()
while gloses:
    word1 = gloses.pop(0)
    word2 = gloses.pop(0)
    
    queue.put(WordPair(word1, word2))
    
while not queue.isempty():
    wordPair = queue.get()
    print("Vad är" , wordPair.lang1, "?")
    answer = input()
    if answer == wordPair.lang2:
        wordPair.numCorrect += 1
        print("Rätt svar!")
    else:
        print("Fel svar!")
    if wordPair.numCorrect < 2:
        queue.put(wordPair)
print("Grattis du har klarat testet!")
