
name = input("Enter your name: ")
marks = int(input("Enter marks: "))
print("Student Name: ", name)
print("Marks: ", marks)

if marks > 85:
  grade = 'A'

elif marks >= 70 and marks < 85:
  grade = 'B'

elif marks >= 50 and marks < 70:
  grade = 'C'

else :
  grade = "Fail"

print("Grade: ", grade)
