print("Student Marks Calculator")

name = input("Enter student name: ")

Telugu = int(input("Enter Telugu marks: "))
Hindi = int(input("Enter Hindi marks: "))
English = int(input("Enter English marks: "))
Maths = int(input("Enter Maths marks: "))
Science = int(input("Enter Science marks: "))
Social = int(input("Enter Social marks: "))

total = Telugu + Hindi + English + Maths + Science + Social
average = total / 6

print("Student Name:", name)
print("Total Marks:", total)
print("Average Marks:", round(average, 2))

if Telugu >= 35 and Hindi >= 35 and English >= 35 and Maths >= 35 and Science >= 35 and Social >= 35:
    print("Result: PASS")

    if average >= 75:
        print("Grade: A")
    elif average >= 60:
        print("Grade: B")
    elif average >= 50:
        print("Grade: C")
    else:
        print("Grade: D")
else:
    print("Result: FAIL")