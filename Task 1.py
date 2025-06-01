No = int(input("Enter the Number : "))

def fact(No):
  if No<0:
      print("Factorial doesnt exist for negative number")
  elif No==1:
      return 1
  else:
      return No*fact(No-1)


ret = fact(No)

print(f"factorial of {No} is {ret}")