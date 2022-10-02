class Table:
    def __init__(self, *kwargs):
        self.v = kwargs #using #kwargs to give values(unpackage named parametres)
  

class RectT(Table):
    
    def SquareR(self):
        length, width  = self.v
        return length*width

class OvalT(Table):
    
    def SquareO(self):
        r, = self.v
        return 3.14*r**2
    
    
t = RectT(10,16)
print(t.SquareR())#call always with ()  - without () will show bouund method!!
t2 = OvalT(5.6)
print(t2.SquareO())
