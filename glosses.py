#encoding: utf-8
   
class WordPair():
    def __init__(self, l1, l2):
        self.lang1 = l1
        self.lang2 = l2
        self.numCorrect = 0

    def __str__(self):
        return "<Wordpair l1 = %s, l2 = %s>" % (self.lang1, self.lang2)

    # lägg till fler attribut och metod(er) om ni vill!
    
