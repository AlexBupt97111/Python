f_one = open("Hello.txt", "w") 
f_one.write("Hello worlds and neighboring  galaxies") 
f_one.close() 

def longest_one(file): 
    a = open(file, "r") 
    parts = a.read().split() 
    max_len =  parts[0]
    for word in parts:
        if len(word) > len(max_len):
            max_len = word
    return (max_len)
print(longest_one("Hello.txt"))
