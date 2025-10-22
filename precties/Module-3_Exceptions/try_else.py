try:
    a = int(input("Enter a number: "))
    b = int(input("Enter b number: "))
    print("sum is : ",a+b)
except Exception as e:
    print("Error is: ", e)
else:
    print("mul is : ",a*b)