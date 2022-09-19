def check_number():
    number = input("Input phone number:\n")
    temp = number.replace('(' ,'').replace(')', '').replace('+', '') 
    temp_p = temp.isdigit()
    if (number[0]=='+') or (number[0]=='3') and len(temp)==12:
        print("Ukrainian phone number")
    else:
	print("Number of other country")
	
check_number()
