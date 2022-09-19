import random
a = []
for i in range(20):
    a.append(random.randint(1, 10))    
max_el = a[0] 
max_count = a.count(max_el) 
for el in a:
    if a.count(el) > max_count:
        max_count = a.count(el)
        max_el = el

#print(a)
print("Element", max_el, "meet", max_count, "times")
