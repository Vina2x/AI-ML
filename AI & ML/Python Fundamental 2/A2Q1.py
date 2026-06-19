salary= int(input("Enter salary: "))

if (salary<30000):
    tax= salary*0.05
    print("Your total payable tax is: ", tax)
elif (salary>=30000 and salary<70000):
    tax= salary*0.15
    print("Your total payable tax is: ", tax)

else:
    tax= salary*0.25
    print("Your total payable tax is: ", tax)