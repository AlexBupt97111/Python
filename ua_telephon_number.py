u = input("Input telephone number:\n")
temp = u.replace('(' ,'').replace(')', '').replace('+', '') 
temp_p = temp.isdigit()
if (u[0]=='+') or (u[0]=='3') and len(temp)==12:
	print("Ukrainian telphone number")
else:
	print("Number of other country")
