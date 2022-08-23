d = {1:"Monday",
     2:"Tuesday",
     3:"Wednesday",
     4:"Thursday",
     5:"Friday",
     6:"Saturday",
     7:"Sunday"
  
}
num = int(input("Input number in range 1-7: "))
print(num," =>",  d.get(num))
