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

        if parachute[0] == "   0": #loses the game
            parachute[0] == "   X"
        else:
            parachute.pop(0)
