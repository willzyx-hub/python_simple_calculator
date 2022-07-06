# No copyrght file
# In order to make sure the code run perfectly you must run it on Terminal with your preferred shell i recommend bash / sh
print("Welcome To simple calculator")
print("Select operation for Calculator:")
print("1. Add Number")
print("2. Subtract Number")
print("3. Multiply")
print("4. Divide")

operation = input()

if operation == "1":
      # code for adding number
      num1 = input("Enter first number to calculate :")
      num2 = input("Enter second number to calculate :")
      print("The result is " + str(int(num1) + int (num2)))
      print("Calculation is Done !")
elif operation == "2":
      num1 = input("Enter first number to calculate :")
      num2 = input("Enter second number to calculate :")
      print("The result is " + str(int(num1) - int (num2)))
      print("Calculation is Done !")
      # code for subtract
elif operation == "3":
      num1 = input("Enter first number to calculate :")
      num2 = input("Enter second number to calculate :")
      print("The result is " + str(int(num1) * int (num2)))
      print("Calculation is Done !")
      # code for division
elif operation == "4":
      num1 = input("Enter first number to calculate :")
      num2 = input("Enter second number to calculate :")
      print("The result is " + str(int(num1) / int (num2)))
      print("Calculation is Done !")
else:
      print("Can not read user input.")