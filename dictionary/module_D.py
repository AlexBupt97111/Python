d = {"car":"авто", "house":"дім", "road":"дорога","language":"мова"}
def Translate_word():
    a = input("Input word by English to translate: ")
    a = d.get(a) #to translate (get value by key)
    print(a)

def Add_word():
    a = input("Input word by English: ")
    b = input("Input word by Ukrainian: ")
    d.setdefault(a,b) #add in console but not in dict!!! use d.update()
    print("Add one")
    print(d)
           
def Delete_word():
    a = input("Input word by English to delete notation: ")
    d.pop(a)
    print(d)
    
def ShowDict():
    for i in d:
        print(i)

