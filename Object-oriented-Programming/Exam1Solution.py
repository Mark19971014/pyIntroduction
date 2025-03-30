class Residence:
#initiator/constrcutor
   #f()
    def __init__(self, number : int, size : float,type : str):
        
        self.number = number
        self.size = size
        self.type = type
    

    def getNumber(self):
        return self.number


room1 = Residence(1,11,"Basecamp")
print(room1.getNumber())