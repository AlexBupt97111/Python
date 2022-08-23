a = input("Input name: ")
b = int(input("Input age: "))
if a.isalpha() and a.istitle():
    name = a
else:
    print("Check data. Use only literals for name and first letter - title one.")
if  0 <= b <= 130:
    age = b
    if age in range(0,10):
        print("Name - ", name, ", age category - child")
    elif age in range(10,25):
        print(name, ", age category - youth")
    elif age in range(25,44):
        print(name, ", age category - young")
    elif age in range(44, 60):
        print(name, ", age category - middle")
    elif age in range(60,75):
        print(name, ", age category - aged")
    elif age in range(75,90):
        print(name, ", age category - old")
    elif age > 90:
        print(name, ", age category - long-lived")
    
else:
    print("Check data. Use only odd numbers and numbers less 130")
