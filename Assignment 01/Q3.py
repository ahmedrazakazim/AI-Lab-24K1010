students = {}
for var in range(3):
  name = input("Enter student name: ")
  marks = int(input("Enter marks: "))
  students[name] = marks

print("Student Records: ")

for name in students.keys():
  print(name, " : ", students[name])
  
