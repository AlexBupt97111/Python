def check_number():
    number = input("Enter the phone number in full, including symbol +"" :\n")
    temp = number.replace('(' ,'').replace(')', '').replace('+', '') 
    temp_p = temp.isdigit()
    if (number[0] == '+') and (number[1] == '3', number[2] == '8', number[3] == '0') and len(temp) == 12:
        print("Ukrainian phone number")
    else:
	print("Number of other country")
	
check_number()
