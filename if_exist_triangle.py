def check_triangle():
    leg_1 = float(input("Input length of first triangle's side: "))
    leg_2 = float(input("Input length of second triangle's side: "))
    hypotenuse = float(input("Input length of third triangle's side: "))
    if  leg_1 + leg_2 > hypotenuse and leg_1 + hypotenuse > leg_2 and leg_2 + hypotenuse > leg_1:
        print("This triangle exist")
    else:
        print("Not exist")  
      
check_triangle()
