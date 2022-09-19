def check_name():
    name = input("Input name: ")
    if name.isalpha() and name.istitle():
        print("Ok")
    else:
        print("Some mistakes. Check it.")
                
check_name()
