import random 

N, M = (5, 10) # N - size of field(5x5), M - count  of mines

def createGame(PM): 
    rng = random.Random() 
  
    n = M 
    while n > 0: 
        i = rng.randrange(N) 
        j = rng.randrange(N)
        if PM [i * N + j] != 0: 
            continue
        PM[i * N + j] = -1
        n -= 1 
        
    for i in range(N):
        for j in range(N):
            if PM[i * N + j] == 0:
                PM[i * N + j] = getTotalMines(PM, i, j)
                                               
def getTotalMines(PM, i, j):
    n = 0 
    for k in range(-1, 2):
        for l in range(-1, 2):
            x = i + k
            y = j + l
            if x < 0 or x >= N or y < 0 or y >= N: 
                continue 
            if PM[x * N + y] < 0: 
               n += 1
    return n

def show(field):
    for i in range(N):
        for j in range(N):
            print(str(field[i * N + j]).rjust(3), end = "")
        print() 

def goPlayer():
    flLoopInput = True
    while flLoopInput:
        x, y = input("Input coordinates by gape: ").split() #input int coordinate
        if not x.isdigit() or not y.isdigit():
            print("Incorrent data")
            continue
        
        x = int(x) - 1
        y = int(y) - 1

        if x < 0 or x >= N or y < 0 or y >= N:
            print("Coordinates are outside of field")
            continue

        flLoopInput = False 
    return (x, y)
        
def isFinish(PM,P):
    for i in range(N * N):
        if P[i] != -2 and PM[i] < 0: 
            return -1 #you on mine (-1); game over
    for i in range(N * N):
        if P[i] == -2 and PM[i] >= 0: 
            return 1 #cell is closen and see mine around - go (1)
        
    return -2 #you win (all is open without mines)
                  
def startGame():
    P = [-2] * N * N 
    PM = [0] * N * N 
    
    createGame(PM)
    
    finishState = isFinish(PM, P) 
    while finishState > 0: 
        show(P)
        x, y = goPlayer()
        P[x * N + y] = PM[x * N + y]
        finishState = isFinish(PM, P)

    return finishState 

res = startGame()
if res == -1:
    print("You lose")
else:
    print("You win")
    
print("Game over")





