def add_string(file, string):
    f_one = open(file, "a") 
    f_one.write(string)
    f_one.write("\n")
    f_one.close() 

string = input("Input  string to add it in file: ")
add_string("New.txt", string)
