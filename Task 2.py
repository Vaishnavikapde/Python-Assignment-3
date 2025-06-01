import math
No = int(input("Enter the Number : "))

def fact(No):
  if No<0:
      print("Factorial doesnt exist for negative number")
  else:
      return math.factorial(No)


ret = fact(No)

print(f"factorial of {No} is {ret}")