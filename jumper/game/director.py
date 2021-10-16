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
        self.game()

    def game(self):
        word = self.dictionary.choose_word() #Use random to choose a word
        game = self.dictionary.make_game(word) #Creates a list that displays this "_ _ _ _"

        parachute = self.console.parachute
        head = parachute[len(parachute)-1]

        self.console.print_parachute() #Print the parachute
        while head != "   X":
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
