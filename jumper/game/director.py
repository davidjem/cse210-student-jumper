from game.console import Console 
from game.dictionary import Dictionary
from game.guesser import Guesser
import sys
class Director:
    pass
    def __init__(self):
        self.console = Console()
        self.dictionary = Dictionary()
        self.guesser = Guesser()
    def start_game(self):
        self.console.print_whatever("Welcome to the Jumper game! \nWe are generating a random word and you have to guess letter by letter\nIf you fail you lose a part of your parachute.\nLose your parachute and you die")
        self.game()

    def game(self):
        word = self.dictionary.choose_word() #Use random to choose a word
        game = self.dictionary.make_game(word) #Creates a list that displays this "_ _ _ _"

        parachute = self.console.parachute
        head = parachute[0]

        self.console.print_parachute() #Print the parachute
        while True:
            if "   X" in parachute:
                self.console.lose_screen(word)
                
            letter = self.guesser.guess_letter(word) #Make the user choose a letter within the word
            if letter in word:
                self.guesser.upload_letter(letter, word, game)
                self.console.print_parachute()
                self.console.print_list(game)

            else:
                self.console.delete_parachute()
                self.console.print_parachute()
                self.console.print_list(game)

            self.dictionary.check_if_win(game)

#print(sys.path)
