num = int(input("Enter number to check: "))

if num >50:
  print("The number is Greater than 50")
  if num%2==0:
     print("The number is Even")
  else:
     print("And it's odd")
else:
    print("Number is less than 50")