from datetime import datetime

orders = []
NEXT_ID = 1

def input_nonempty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Enter a value.")

def input_float(prompt, min_value=0.0):
    while True:
        raw = input(prompt).strip()
        try:
            num = float(raw)
            if num < min_value:
                print(f"Value must be ≥ {min_value}.")
                continue
            return num
        except ValueError:
            print("Enter a number.")

def input_int(prompt, min_value=0):
    while True:
        raw = input(prompt).strip()
        try:
            n = int(raw)
            if n < min_value:
                print(f"Value must be ≥ {min_value}.")
                continue
            return n
        except ValueError:
            print("Enter an integer.")

def input_date_ddmmyyyy(prompt):
    while True:
        s = input(prompt).strip()
        try:
            s2 = s.replace("/", "-")
            datetime.strptime(s2, "%d-%m-%Y")
            return s2
        except ValueError:
            print("Enter date in DD-MM-YYYY format.")

def pause():
    input("\nPress Enter to continue...")

def create_order():
    global NEXT_ID
    print("\n=== New Repair Order ===")
    customer = input_nonempty("Customer name: ")
    device = input_nonempty("Device: ")
    issue = input_nonempty("Issue: ")
    due = input_date_ddmmyyyy("Due date (DD-MM-YYYY): ")
    order = {
        "id": NEXT_ID,
        "customer": customer,
        "device": device,
        "issue": issue,
        "due_date": due,
        "status": "Booked",
        "parts": [],
        "repair_fee": 0.0,
        "tax_rate": 18.0,
        "discount": 0.0,
        "bill_total": None,
        "created_at": datetime.now().strftime("%d-%m-%Y %H:%M"),
        "paid": False
    }
    orders.append(order)
    print(f"\nOrder #{NEXT_ID} created.")
    NEXT_ID += 1

def list_orders(show_details=False):
    if not orders:
        print("\nNo orders.")
        return
    print("\n=== Orders List ===")
    for o in orders:
        print(f"#{o['id']:03d} | {o['customer']} | {o['device']} | {o['status']} | Due: {o['due_date']}")
        if show_details:
            print(f"    Issue: {o['issue']}")
            if o["parts"]:
                print("    Parts:")
                for p in o["parts"]:
                    print(f"      - {p['name']} x{p['qty']} @ ₹{p['unit_price']:.2f} = ₹{p['line_total']:.2f}")
            if o["bill_total"] is not None:
                print(f"    Repair Fee: ₹{o['repair_fee']:.2f}")
                print(f"    Tax: {o['tax_rate']:.2f}%")
                print(f"    Discount: ₹{o['discount']:.2f}")
                print(f"    FINAL: ₹{o['bill_total']:.2f}")
            print()

def find_order_by_id(order_id):
    for o in orders:
        if o["id"] == order_id:
            return o
    return None

def add_parts_flow(order):
    print("\n=== Add Parts ===")
    while True:
        name = input_nonempty("Part name: ")
        qty = input_int("Qty: ", 1)
        price = input_float("Unit price ₹: ", 0.0)
        line_total = qty * price
        order["parts"].append({
            "name": name,
            "qty": qty,
            "unit_price": price,
            "line_total": line_total
        })
        print(f"  Added: {name} x{qty} = ₹{line_total:.2f}")
        more = input("Add another part? (y/n): ").strip().lower()
        if more != "y":
            break

def compute_bill_amount(order):
    parts_subtotal = sum(p["line_total"] for p in order["parts"])
    base = parts_subtotal + float(order["repair_fee"])
    tax_amt = base * (float(order["tax_rate"]) / 100.0)
    gross = base + tax_amt
    final = max(0.0, gross - float(order["discount"]))
    return round(final, 2)

def print_invoice(order):
    print("\n" + "=" * 54)
    print("FixTrack Invoice".center(54))
    print("=" * 54)
    print(f"Order #{order['id']:03d}")
    print(f"Customer : {order['customer']}")
    print(f"Device   : {order['device']}")
    print(f"Issue    : {order['issue']}")
    print(f"Due Date : {order['due_date']}")
    print("-" * 54)
    if order["parts"]:
        print("Parts:")
        for p in order["parts"]:
            print(f"  - {p['name']:<20} x{p['qty']:<3} @ ₹{p['unit_price']:<8.2f} = ₹{p['line_total']:<10.2f}")
    else:
        print("Parts: (none)")
    parts_subtotal = sum(p["line_total"] for p in order["parts"])
    print("-" * 54)
    print(f"Parts Subtotal   : ₹{parts_subtotal:,.2f}")
    print(f"Repair Fee       : ₹{order['repair_fee']:,.2f}")
    base = parts_subtotal + order['repair_fee']
    tax_amt = base * (order['tax_rate'] / 100.0)
    print(f"Tax @{order['tax_rate']:.2f}%       : ₹{tax_amt:,.2f}")
    print(f"Discount         : ₹{order['discount']:,.2f}")
    print("-" * 54)
    final = compute_bill_amount(order)
    print(f"FINAL AMOUNT     : ₹{final:,.2f}")
    print("=" * 54)

def billing_flow():
    if not orders:
        print("\nNo orders.")
        return
    oid = input_int("Order ID: ", 1)
    order = find_order_by_id(oid)
    if not order:
        print("Not found.")
        return
    choice = input("Add parts? (y/n): ").strip().lower()
    if choice == "y":
        add_parts_flow(order)
    order["repair_fee"] = input_float("Repair fee ₹: ", 0.0)
    tr = input("Tax rate % (default 18): ").strip()
    if tr:
        try:
            trv = float(tr)
            if trv < 0:
                trv = 18.0
            order["tax_rate"] = trv
        except ValueError:
            order["tax_rate"] = 18.0
    else:
        order["tax_rate"] = 18.0
    order["discount"] = input_float("Discount ₹: ", 0.0)
    order["status"] = "Completed"
    order["bill_total"] = compute_bill_amount(order)
    print_invoice(order)
    paid_ans = input("Payment done? (y/n): ").strip().lower()
    order["paid"] = (paid_ans == "y")
    print("Billing completed!")

def update_status():
    if not orders:
        print("\nNo orders.")
        return
    oid = input_int("Order ID: ", 1)
    order = find_order_by_id(oid)
    if not order:
        print("Not found.")
        return
    print(f"Current status: {order['status']}")
    new_status = input_nonempty("New status: ")
    order["status"] = new_status
    print("Status updated.")

def delete_order():
    if not orders:
        print("\nNo orders.")
        return
    oid = input_int("Order ID to delete: ", 1)
    o = find_order_by_id(oid)
    if not o:
        print("Not found.")
        return
    confirm = input(f"Type YES to delete: ").strip()
    if confirm == "YES":
        orders.remove(o)
        print("Order deleted.")
    else:
        print("Canceled.")

def show_menu():
    print("\n====== FixTrack ======")
    print("1) New Order")
    print("2) List Orders")
    print("3) List Orders (detailed)")
    print("4) Billing")
    print("5) Update Status")
    print("6) Delete Order")
    print("0) Exit")
    print("=======================")

def main():
    print("Welcome to FixTrack!")
    while True:
        show_menu()
        choice = input("Choice: ").strip()
        if choice == "1":
            create_order()
            pause()
        elif choice == "2":
            list_orders(False)
            pause()
        elif choice == "3":
            list_orders(True)
            pause()
        elif choice == "4":
            billing_flow()
            pause()
        elif choice == "5":
            update_status()
            pause()
        elif choice == "6":
            delete_order()
            pause()
        elif choice == "0":
            print("Bye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...")
