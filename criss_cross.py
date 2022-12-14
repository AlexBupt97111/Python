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
Field = create_field(3, 3, "_") #3 - size of field: "_" - temporary game symbol
                              #gamefield - global variable; symb"_" - required positional argument

def show_field(Field):
    for el in Field:
        print(*el)
                
def goPlayer(symb):
    gou = "" 
    while gou != "go":
        try:
            (in_line, in_column) = input("Enter line(x) and column(y). Example(1 3): ").replace(",", " ").split()
            x, y = int(in_line) - 1, int(in_column) - 1 
            if x not in range(0, 3) or y not in range(0, 3):
               print("\n Uncorrect coordinates. Use integer numbers in range 1-3 \n")
            else:    
                if Field[x][y] == "_":
                    Field[x][y] = symb  
                
                    gou = "go"
                    show_field(Field)
                    print()
                    return x, y 
                               
                else:
                    print("\n This cell is fill! \n")
        except ValueError:
            print("Enter two values.  Example: 1 2")
    
def goComp(symb): #condition for computer
    rng = random.Random()
    gou = ""
    
    while gou != "go": 
        x = rng.randrange(len(Field))
        y = rng.randrange(len(Field[0])) 
        
        if Field[x][y] != "_":
            continue
        else:
            Field[x][y] = symb
            gou = "go"  
            show_field(Field)
            print()
    return x, y
    
def ifFinish(x, y, symb):
    if(Field[x][0] == Field[x][1] == Field[x][2] == symb) or (Field[0][y] == Field[1][y] == Field[2][y] == symb) or (Field[0][0] == Field[1][1] == Field[2][2] == symb) or (Field[0][-1] == Field[1][-2] == Field[2][0] == symb):
        return 1
    else:
        return 0
    
def createGame():   
    symb = input("Choose symbol X or 0 (zero).\nIf choose X - you go first.\nIf 0 - program go first: ") 
    comp = "X" if symb == "0" else "0"

    win = False
    count = len(Field) * len(Field[0])
    
    while win == False and count>0:

        if symb == "X": #if player chose X - he goes first
            count -= 1
            x, y = goPlayer(symb) #input symbol in position of Player(coordinates x;y)
            win += ifFinish(x, y, symb)

            if win == False and count > 0:
                count -= 1        
                x, y = goComp(comp)
                win += ifFinish(x, y, comp)

        if symb == "0": 
            count -= 1                    
            x, y = goComp(comp)
            win += ifFinish(x, y, symb = comp)        
            
            if win == False and count > 0:
                count -= 1
                x, y = goPlayer(symb)
                win += ifFinish(x, y, symb)  

    if win != False:
        print("Win %s"% Field[x][y])
    else:
        print("Battle draw")

createGame()
