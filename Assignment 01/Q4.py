choice = 0
while (choice != 3):
  print("1. Add two numbers")
  print("2. Subtract two numbers")
  print("3. Exit")
  choice = int(input("Enter your choice: "))

  if choice == 3:
    break

  else:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if choice == 1:
      print("Result: ", num1 + num2)
    else:
      print("Result: ", num1 - num2)
