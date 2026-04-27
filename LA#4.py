print("Eligibility Checker Program")
print("===========================")
user_age=int(input("Enter your age: "))
user_ID= input("Do you have an ID (Yes/No): ")

if user_age>=60 and user_ID == 'Yes':
    print('Eligible for senior discount!')
elif user_age>18 and user_ID == 'Yes':
    print('Eligible!')
else:
    print('Not Eligible!')
