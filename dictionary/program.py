import ModuleD

while True:
    
    x = int(input("""Input certain number for certain action:
              1 - Translate word;
              2 - Add word;
              3 - Delete word;
              0 - Finish work:
"""))

    if x == 1:
        ModuleD.Translate_word()      
    elif x == 2:
        ModuleD.Add_word()             
    elif x == 3:
        ModuleD.Delete_word()   
    elif x == 0:
        print("Finish work")
        break
