class Guesser:
    letters = []
    def __init__(self):
        pass
    def guess_letter(self, word):
        letters = self.letters
        letter = input("Choose a letter: ")
        
        if letter in letters:
            print("You chosen a repeated letter")
            self.guess_letter(word)
            return letter
            
        else:
            letters.append(letter)
            return letter

  
    def upload_letter(self, letter, word, list):
        index = word.index(letter) #Know what place have the chosen letter in our word
        list[index] = letter

