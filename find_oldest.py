import random
names = ["Simba", "Murchik", "Murka", "Masya", "Pushok"]
cats  = [] 
for i in range(5): 
    cat = {"name": names[i],
           "age": random.randint(1, 15) 
          }
    cats.append(cat) 
print(cats)

max_cat = cats[0] 
for cat in cats:
    if max_cat.get("age") < cat.get("age"):
        max_cat = cat
print(max_cat)
