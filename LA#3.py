print('Temperature Checker')
temp_inpt=int(input("Enter temperature today: "))

if temp_inpt>30 :
    print("'Hot day! Stay hydrated.'")
elif temp_inpt>10:
    print("'Pleasant weather!'")
elif temp_inpt<=10:
    print("May bagyo ba? O may bago na?")
else:
    print("Invalid Input")
