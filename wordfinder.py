

import random

class WordFinder:
    def __init__(self, file):
        file = open(file, 'r')
        self.counter = 0
        self.words = [line.strip("\n") for line in file]
        self.counter = len(self.words)
        print("Words read: " + str(self.counter))
    def read(self):
        # prints all words in file
        for line in self.words:
            print(line)
       
      
    def random(self):
        #pick a random word 
        random_word = random.choice(self.words)
        print(random_word)
        return random_word
    
    #def words_read(self):
         #increment and print counter

word_find = WordFinder("./words.txt")
#word_find.read()
#word_find.random()
