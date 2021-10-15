"""  
  ___  
 /___\ 
 \   / 
  \ /  
   0   
  /|\  
  / \  
       """
class Console:
    parachute =["  ___"," /___\ "," \   /","  \ /","   0"]   

    def __init__(self):
        pass
    
    def delete_parachute(self):
        parachute = self.parachute

        if parachute[0] == "   0": #Loses the game and changes the head to an x
            parachute[0] == "   X"
        else:
            parachute.pop(0)

    def print_parachute(self):
        parachute = self.parachute
        while number != 0:
            print("      \n", )