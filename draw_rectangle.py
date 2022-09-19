def rectangle(length, width): 
    i = 1 
    j = 1 
    while i <= length:
        j = 1 
        while j <= width: 
            print("*", end = '') 
            j = j + 1 
        print() 
        i = i + 1    
length = int(input("Input number for height: "))
width = int(input("Input number for width: "))  

rectangle(length, width)
