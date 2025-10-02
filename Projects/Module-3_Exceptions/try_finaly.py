try:
    a = int(input("Enter a number: "))
    b = int(input("Enter b number: "))
    print("sum is : ",A+b)
except Exception as e:
    print("Error is: ", e)
finally:
    print("mul is : ",a*b)