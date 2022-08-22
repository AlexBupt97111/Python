import random # to generate random numbers

N,M = (5 , 10)# N - the size of the playing field, M -  number of mines, global variable (constants)

def createGame(PM): #PM - fun createGame places mines on the field PM  (so PM - is argument)
    """ Функція створення ігрового поля: розташування мін
    і підрахунок кількості мін навколо клітинок без мін (релізація знизу)
    """ 
    rng = random.Random()#module random named rng - to generate falserandom numbers
    
    #process of filling cells with  mines
    n = M #n - number of mines already placed ; n - counter
    while n > 0: #process of filling cells with  mines
        i = rng.randrange(N) # random int [0;N) from 0 to N-1, to be in range of gamefield
        j = rng.randrange(N)
        if PM [i*N+j] !=0: # ця клітинка не дорівнює нулю  і там щось поставили
            continue
        PM[i*N+j] = -1#ставимо міну (значення -1)
        n-=1 #зменшуємо к-сть на 1

    #check neighbours cells and call getTotalMines 
    for i in range(N):
        for j in range(N):
            if PM[i*N+j] == 0:#empty cell, without mines
                PM[i*N+j] = getTotalMines(PM, i, j)# for cell with index(i;j) assign the value of the function

    """  additional fun getTotalMines - calculate the number of mines aroud cell with indexes(i,j)  """                                                     

def getTotalMines(PM, i, j): #calculate the number of mines aroud cell with indexes(i,j)
    n=0 #counter of mines
    for k in range(-1,2): #range from -1 to 1 (2  - not include)
        for l in range(-1,2):
            x = i+k
            y = j+l # with help of x and y check all the cells around the current one
            if x < 0 or x >= N or y < 0 or y >= N: # if x & y are go beyond the field
                continue #nothing to do
            if PM[x*N+y] < 0: #if position of (x;y) in field and less then zero - mine here and counter of mines +=1
               n+=1
    return n

def show(field):
    """ Відображає поточний стан ігрового поля """
    for i in range(N):
        for j in range(N):
            print ( str(field[i*N+j]).rjust(3), end = "") # number - in string and r.just,  end ="" - to not locate in new string
        print() 

def goPlayer():
    """ Функція призначена для вводу користувачем координат
    закритої клітинки ігрового поля
    """
    flLoopInput = True #to start function
    while flLoopInput:#to input correct data
        x, y = input("Введіть координати через пробіл: ").split() #to input int coordinate
        if not x.isdigit() or not y.isdigit(): #to check correctly input data
            print("Координати введені неправильно")
            continue #return to start of cycle
        
        x = int(x)-1 #if all okay - we convert; why -1-because user input numbers include  N ( but must be (N-1)
        y = int(y)-1

        if x < 0 or x >= N or y < 0 or y >= N: #write bounds of field
            print("Координати виходять за межі поля")
            continue

        flLoopInput = False #if all okay -  we stop the cycle
    return (x,y)
        

def isFinish(PM,P):
    """ Визначає поточний стан гри: виграв, програв,
    гра продовжується
    """
    for i in range(N*N):
        if P[i] != -2 and PM[i] < 0: return -1 #you on mine (-1); game over
    for i in range(N*N):
        if P[i] == -2 and PM[i] >= 0: return 1 #cell is closen and see mine around - go (1)
        
    return -2 #you win (all is open without mines)
            
        
      
def startGame(): # first step (need: lists, creator, check of game (cycle while - isFinish (with show & go)))
    """ Функція запуску гри: відображаєтьься ігрове поле,
        гравець відкриває буь-яку закриту клітинку, перевірка результату
        на наявність  або відсутність міни 
    """
    P = [-2]*N*N # lokal,to show current state of the game (N*N - size of field); all cells are closen
    PM = [0]*N*N # lokal variable, list  with location of mines (before filling - all empty)
    
    createGame(PM)#1  - locate mines on field of game, so PM like argument (P & PM - all that need to start)
    
    finishState = isFinish(PM,P) #additional variable
    while finishState > 0: #2  - check the current state of the game #(cycle)loop to call auxiliary functions
        show(P)#2.1  - show the current state return coordinates
        x,y = goPlayer()#2.2 - input & return coordinates
        P[x*N+y] = PM[x*N+y] # open point (x,y) on field P
        finishState = isFinish(PM,P)

    return finishState 

res = startGame()
if res == -1:
    print("Ви програли")
else:
    print("Ви виграли")
    
print("Гра завершена")#завершення гри (startGame ,print("Гра завершена") -  відмітили своєрідні межі, поле дії)

#while - loop(cycle) to call auxiliary functions (create,show, go, is finish)



