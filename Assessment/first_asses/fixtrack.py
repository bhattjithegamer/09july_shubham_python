#sir do not give me copy right bcz it is created menuly

orders = []

def new_order():
    print("====your new order=====")
    name = input("enter name : ")
    device = input("enter divice : ")
    issue = input("what is your problem : ")
    date = input("due date(dd-mm-yyyy) : ")
    if len(date) == 10 and date[2] == '-' and date[5] == '-' and date[:2].isdigit() and date[3:5].isdigit() and date[6:10].isdigit():
        print
    else:
        print("Invalid format do again")
        exit()
    

    order2 = {
        "customer_name" : name,
        "device_type" : device,
        "issue" : issue,
        "due_date" : date
    }

    orders.append(order2)
    print("your order booked ")

def all_order():
    print("\n ===orders=== ")
    if not orders:
        print("there is no orders ")
    else:
        index = 1
        for order in orders:
            print(f"\n order {index} : ")
            print(f"customer name : {order['customer_name']}")
            print(f" Device Type: {order['device_type']}")
            print(f" Issue: {order['issue']}")
            print(f" Due Date: {order['due_date']}")
            index += 1

def generate_bill():
    if not orders:
        print("there are no orders for bill")
        return
    
    all_order()
    order_no = int(input("enter order num to generate bill: "))

    if order_no < 1 or order_no > len(orders):
        print("invelid order number ")
        return

    order = orders[order_no - 1]

    cost = float(input("Enter parts cost: "))
    repairing = float(input("Enter repair charge: "))

    subtotal = cost + repairing
    tax = subtotal * 0.18  
    discount = float(input("Enter discount : "))
    
    total = subtotal+tax-discount

    print("\n===== Invoice =====")
    print(f"Customer: {order['customer_name']}")
    print(f"Device: {order['device_type']}")
    print(f"Issue: {order['issue']}")
    print(f"Due Date: {order['due_date']}")
    print("----------------------------")
    print(f"Parts Cost: {cost}")
    print(f"Repair Charge: {repairing}")
    print(f"Subtotal: {subtotal}")
    print(f"Tax (18%): {tax:.2f}")
    print(f"Discount: {discount}")
    print("----------------------------")
    print(f"Total Amount: {total:.2f}")
    print("============================")

def menu():
    while True:
        print("==========repairing=========")
        print("1- new order")
        print("2- generate bill")
        print("3- view all orders")
        print("4- exit")

        choice = input("enter your choice : ")

        if choice == '1':
            new_order()
        elif choice == '2':
            generate_bill()
        elif choice == '3':
            all_order()
        elif choice == '4':
            print("Exiting FixTrack. Thank You")
            break
        else:
            print("enter velid")
menu()