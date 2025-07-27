class WrongDnaError(Exception):
    print("Error")
class Father:
    def __init__(self,last_name):
        self.title=last_name

class Son(Father):
    def DNA_check(self,last_name):
        self.last_name=last_name
        Father.__init__(self,last_name)
        if(self.title!="Biswal"):
          print("the dna is not match")
          raise WrongDnaError ("dna not match")
            
          
son1=Son("name")
try:
    son1.DNA_check("Das")
except WrongDnaError as e:
    print("Exception Raised:", e)