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
        parachute.pop(0)

    