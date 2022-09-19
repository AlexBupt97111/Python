class Rectangle:
    def __init__(self, w, h):
        self.__w = w
        self.__h = h

    def getPer(self): #only 1 name of  method for all
        return 2 * (self.__w + self.__h) #but different funcional(python understand)

class Square:
    def __init__(self, a):
        self.__a = a

    def getPer(self):
        return 4 * self.__a

r1 = Rectangle(1, 2)
r2 = Rectangle(3, 4)
print(r1.getPer(), r2.getPer())

s1 = Square(10)
s2 = Square(20)
print(s1.getPer(), s2.getPer())

geo = [r1, r2, s1, s2]
for g in geo:
    print(g.getPer())
        
