year = int(input("Input year for checking: "))
if year % 4 == 0  or year % 400 == 0:
    print( year," - intercalary" )
elif year % 100 == 0:
    print (year, " - not intercalary")   
else:
    print (year, " - not intercalary")
