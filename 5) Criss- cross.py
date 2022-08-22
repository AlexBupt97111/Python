import random

def create_field(line, colmn, symb):#creating two-dimensional array; all arguments are required
    """Створення двомірного масиву(поля),наповненого вказаними символами"""
    field = []#create empty field
    for i in range(line): #horizontally range 
        internal = []#add empty line (rectangle)    
        for j in range(colmn): #vertical range(column)   
            internal.append(symb)#add symbols in every microsquare
        field.append(internal) # add in mtrx ready elements
    return field #return field after every gamemove(iteration)
"_"
F = create_field(3,3,"_")  #3 - size of field: "_" - temporary game symbol
                           #gamefield - global variable; symb"_" - required positional argument

def show_field(F):
    """(Функція відображення поточного стану поля.
        Виводить двомірний масив у вигляді матриці.
    """
    for el in F:
        print(*el)
                
def goPlayer(symb):#condition for gamer
    gou = "" #to start function (same to flLoopInput in game Pioneer)
    while gou != "go":
    
        (in_line, in_column) = input("введіть рядок (1-3), стовпець(1-3): ").replace(",", " ").split()
        x,y = int(in_line)-1, int(in_column)-1 #why -1-because user input numbers include N( but must be (N-1)
        
        if x not in range(0,3) or y not in range(0,3):#checking is correctly input data
            print("\nНевірні координати \n")
        else:    
            if F[x][y] =="_":
                F[x][y] = symb  
                
                gou = "go"
                show_field(F)#show created gamefield and current state of game
                print()
                return x, y #show the player's move and symbol on field 
                               
            else:
                print("\nЦя клітинка зайнята!\n")
    
def goComp(symb):#condition for computer
    rng = random.Random()
    gou = ""
    
    while gou != "go": 
        x = rng.randrange(len(F))
        y = rng.randrange(len(F[0])) 
        
        if F[x][y]!="_":
            continue
        else:
            F[x][y]= symb
            gou = "go"  
            show_field(F)
            print()
    return x,y
    
def ifFinish( x,y, symb):# add terms of winning and check them during the game
    if(F[x][0]==F[x][1]==F[x][2]==symb)or(F[0][y]==F[1][y]==F[2][y]==symb)or(F[0][0]==F[1][1]==F[2][2]==symb)or(F[0][-1]==F[1][-2]==F[2][0]==symb):
        return 1
    else:
        return 0
    
def createGame():
    """Створення ігрового поля, розподіл символів
     - гравець вибирає хрестик чи нулик. 
     Якщо комп'ютеру дістався хрестик - перший хід за ним
    """    
    symb = input("Виберіть символ  + або 0 (нуль): ") 
    comp = "+" if symb =="0" else "0"

    win = False
    count = len(F)*len(F[0])
    
    while win ==False and count>0: #prescribe the conditions of the game #and action for the player and the computer;

        if symb=="+":#if player chose + - he goes first
            count-=1
            x,y = goPlayer(symb)#input symbol in position of Player(coordinates x;y)
            win += ifFinish(x,y, symb)

            if win == False and count>0:
                count-=1        
                x,y = goComp(comp)
                win += ifFinish(x,y, comp)

        if symb=="0": 
            count-=1                    
            x,y = goComp(comp)
            win += ifFinish(x,y,symb=comp)        
            
            if win == False and count>0:
                count-=1
                x,y = goPlayer(symb)
                win += ifFinish(x,y, symb)  

    print("Гра завершена, виграв %s"% F[x][y]) if win != False else print("Бойова нічия")
createGame()
