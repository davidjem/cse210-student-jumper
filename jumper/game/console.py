class Console:
    parachute =["  ___"," /___\ "," \   /","  \ /","   0"]   

    def __init__(self):
        pass

    def delete_parachute(self):
        parachute = self.parachute

        if len(parachute) <= 1:
            parachute[0] = "   X"
            
        else:
            parachute.pop(0)  #Delete the upper part of the parachute

    def print_parachute(self):
        parachute = self.parachute
        
        print() #Empty space.
        number = 0
        while number != (len(parachute)):    #Print the elements of the list
            print (parachute[number])
            number += 1
        print("  /|\  ")
        print("  / \  ")

    def print_list(self, lista):
        strlist = " ".join(lista)
        print(strlist)

    def lose_screen(self, word):
        print("You lost the game")
        print(f"The word was {word}")
        input("Press any key to exit")
        exit()

    def print_whatever(self, whatever):
        print(whatever)
    
"""  
  ___  
 /___\ 
 \   / 
  \ /  
   0   
  /|\  
  / \  
       """
