mark = int(input("Enter Total Marks : "))

if mark>90 and mark<=100:
    grade = "Excellent"
elif mark>=70 and mark<=90:
    grade = "Good"
else:
    grade = "Fail"

print("You Are " + grade)