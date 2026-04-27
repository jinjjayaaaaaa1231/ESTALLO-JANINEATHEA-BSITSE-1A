print("Grade Calculator Program")
print("===========================")
print(" A = 100-90")
print(" B =  89-80")
print(" C =  79-70")
print(" D =  69-60")
print(" F = Below 60")
student_grade=int(input("Enter Your Grade: "))


if student_grade==100 or student_grade >=98:
    print(f'Score:',student_grade,"->  Grade: A+  Excellent!")
elif student_grade==97 or student_grade >=93:
    print(f'Score:',student_grade,"->  Grade: A  Excellent!")
elif student_grade==92 or student_grade >=90:
    print(f'Score:',student_grade,"->  Grade: A-  Excellent!")
elif student_grade==89 or student_grade >=87:
    print(f'Score:',student_grade,"->  Grade: B+ Very Good!")
elif student_grade==86 or student_grade >=83:
    print(f'Score:',student_grade,"->  Grade: B  Very Good!")
elif student_grade==82 or student_grade >=80:
    print(f'Score:',student_grade,"->  Grade: B- Very Good!")
elif student_grade==79 or student_grade >=77:
    print(f'Score:',student_grade,"->  Grade: C- - Good Job!")
elif student_grade==76 or student_grade >=73:
    print(f'Score:',student_grade,"->  Grade: C Good Job!")
elif student_grade==72 or student_grade >=70:
    print(f'Score:',student_grade,"->  Grade: C+ - Good Job!")
elif student_grade==69 or student_grade >=67:
    print(f'Score:',student_grade,"->  Grade: D - Good!")
elif student_grade==66 or student_grade >=60:
    print(f'Score:',student_grade,"->  Grade: D - Good!")
else:
    print(f'Score:',student_grade,"->  Grade: F - Better Luck Next Time!")
