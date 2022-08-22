import random

def create_field(line, colmn, symb): #creating two-dimensional array;
    field = []
    for i in range(line):
        internal = []  
        for j in range(colmn):   
            internal.append(symb)
        field.append(internal)
    return field 
"_"
F = create_field(3,3,"_") #3 - size of field: "_" - temporary game symbol
                          #gamefield - global variable; symb"_" - required positional argument

def show_field(F):
    for el in F:
        print(*el)
                
def goPlayer(symb):
    gou = "" 
    while gou != "go":
    
        (in_line, in_column) = input("input raw(digits 1-3), column(digits 1-3): ").replace(",", " ").split()
        x,y = int(in_line)-1, int(in_column)-1 
        
        if x not in range(0,3) or y not in range(0,3):
            print("\n Uncorrect coordinates \n")
        else:    
            if F[x][y] =="_":
                F[x][y] = symb  
                
                gou = "go"
                show_field(F)
                print()
                return x, y 
                               
            else:
                print("\n This cell is fill! \n")
    
def goComp(symb): #condition for computer
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
    
def ifFinish( x,y, symb):
    if(F[x][0]==F[x][1]==F[x][2]==symb)or(F[0][y]==F[1][y]==F[2][y]==symb)or(F[0][0]==F[1][1]==F[2][2]==symb)or(F[0][-1]==F[1][-2]==F[2][0]==symb):
        return 1
    else:
        return 0
    
def createGame():   
    symb = input("Choose symbol + або 0 (zero): ") 
    comp = "+" if symb =="0" else "0"

    win = False
    count = len(F)*len(F[0])
    
    while win == False and count>0:

        if symb=="+": #if player chose + - he goes first
            count-=1
            x,y = goPlayer(symb) #input symbol in position of Player(coordinates x;y)
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

    print("Game over, win %s"% F[x][y]) if win != False else print("Battle draw")
createGame()
