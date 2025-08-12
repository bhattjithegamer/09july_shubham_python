def food():
    a = input("enter your name ")
    b =int(input("enter your NO."))
    if b > 11:
        print("enter velid number")

    print("==============menu===============")
    print("1. Pizza -rs.500")
    print("2. Burger -rs.300")
    print("3. French Fries -rs.200")
    print("4. Chocolate -rs.400")
    print("5. ice Cream -rs.300")
    
    user = int(input("enter your choice (1-5): "))

    if user == 1:
        print("your order is Pizza")
        price = 500
    elif user == 2:
        print("your order is Burger")
        price = 300
    elif user == 3:
        print("your order is French Fries")
        price = 200
    elif user == 4:
        print("your order is Chocolate")
        price = 400
    elif user == 5:
        print("your order is Ice Cream")
        price = 300
    else:
        print("Invalid choice! Please try again.")

    quntity = int(input("enter quantity: "))
    total = quntity * price
    print("Total cost: ", total)
    gst = total * 18 / 100
    print("GST: ", gst)

    fulltotal = total + gst
    print("Total with GST: ", fulltotal)
   
food()