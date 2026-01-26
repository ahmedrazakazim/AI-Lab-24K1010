n = int(input("Enter number of marks to be added: "))
i = 0
list1 = []
while (i!=n):
  marks = int(input("Enter marks: "))
  list1.append(marks)
  i = i + 1

def calculate_average(list1):
  print("Marks: ", list1)
  average = 0 
  for mark in list1: 
    average = average + mark

  if n > 0:
    average = average / n
  else:
    average = 0
  print("Average Marks: ", average)

calculate_average(list1) 
