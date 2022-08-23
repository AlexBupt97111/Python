def rectangle(a,b): 
    i = 1 
    j = 1 
    while i <= a:
        j = 1 
        while j <= b: 
            print("*", end = '') 
            j = j + 1 
        print() 
        i = i + 1    
a = int(input("Input number for height: "))
b = int(input("Input number for width: "))        
rectangle(a,b)
