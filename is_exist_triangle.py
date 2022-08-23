a = float(input("Input length of first triangle's side: "))
b = float(input("Input length of second triangle's side: "))
c = float(input("Input length of third triangle's side: "))
if  a + b > c and a + c > b and b +c > a:
    print("This triangle exist")
else:
    print("Not exist")  
