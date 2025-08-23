"""
FixTrack — A simple Python console program to track gadget repair orders and generate bills.

Core goals:
- Repair Order Booking (customer name, device, issue, due date)
- Billing (parts + repair fee + tax + optional discount → final amount)
- In‑memory storage (lists & dictionaries)
- Clean, function‑based code with loops and basic validation
- Clear, formatted bill printing

Run:  python fixtrack.py
Python: 3.8+
"""
import datetime as dt
import itertools
from typing import List, Dict, Any

# ---------------------------
# In-memory storage
# ---------------------------
ORDERS: List[Dict[str, Any]] = []
_id_counter = itertools.count(1001)

# ---------------------------
# Helpers
# ---------------------------

def now_date_str() -> str:
    return dt.datetime.now().strftime("%Y-%m-%d %H:%M")

def input_non_empty(prompt: str) -> str:
    while True:
        val = input(prompt).strip()
        if val:
            return val
        print("❗ This field cannot be empty. Please try again.")

def input_float(prompt: str, min_val: float | None = None) -> float:
    while True:
        raw = input(prompt).strip()
        try:
            val = float(raw)
            if min_val is not None and val < min_val:
                print(f"❗ Value must not be less than {min_val}.")
                continue
            return val
        except ValueError:
            print("❗ Enter a valid number (e.g., 499.99).")

def input_int(prompt: str, min_val: int | None = None) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            val = int(raw)
            if min_val is not None and val < min_val:
                print(f"❗ Value must not be less than {min_val}.")
                continue
            return val
        except ValueError:
            print("❗ Enter a valid integer (e.g., 1, 2, 3).")

def parse_due_date() -> str:
    while True:
        s = input("Due date (YYYY-MM-DD): ").strip()
        try:
            dt.datetime.strptime(s, "%Y-%m-%d")
            return s
        except ValueError:
            print("❗ Invalid date format. Example: 2025-08-30")

def money(n: float) -> str:
    return f"₹{n:,.2f}"

# ---------------------------
# Core: Order creation & listing
# ---------------------------

def add_order() -> None:
    print("\n=== New Repair Order ===")
    customer = input_non_empty("Customer name: ")
    device = input_non_empty("Device type (e.g., Phone/Laptop/Tablet): ")
    issue = input_non_empty("Issue description: ")
    due_date = parse_due_date()

    oid = next(_id_counter)
    order = {
        "id": oid,
        "created_at": now_date_str(),
        "customer": customer,
        "device": device,
        "issue": issue,
        "due_date": due_date,
        "status": "Pending",
        "parts": [],
        "repair_fee": 0.0,
        "tax_percent": 18.0,
        "discount_percent": 0.0,
        "totals": {
            "parts_total": 0.0,
            "subtotal": 0.0,
            "tax_amount": 0.0,
            "discount_amount": 0.0,
            "grand_total": 0.0,
        },
        "invoice_no": None,
        "completed_at": None,
    }
    ORDERS.append(order)
    print(f"✅ Order created with ID: {oid}")

def list_orders(show_all: bool = True) -> None:
    if not ORDERS:
        print("\n(No orders yet)")
        return
    print("\n=== Orders ===")
    for o in ORDERS:
        if (not show_all) and o["status"] == "Completed":
            continue
        print(
            f"ID: {o['id']} | {o['customer']} | {o['device']} | Due: {o['due_date']} | Status: {o['status']}"
        )

def find_order_by_id(oid: int) -> Dict[str, Any] | None:
    for o in ORDERS:
        if o["id"] == oid:
            return o
    return None

def search_orders() -> None:
    term = input_non_empty("Search by customer/device/issue: ").lower()
    results = [
        o for o in ORDERS
        if term in o["customer"].lower()
        or term in o["device"].lower()
        or term in o["issue"].lower()
    ]
    if not results:
        print("❌ No matching orders found.")
        return
    print("\n=== Search Results ===")
    for o in results:
        print(
            f"ID: {o['id']} | {o['customer']} | {o['device']} | Due: {o['due_date']} | Status: {o['status']}"
        )

# ---------------------------
# Parts & Billing
# ---------------------------

def add_parts_flow(order: Dict[str, Any]) -> None:
    print("\n— Add Parts —")
    n = input_int("How many different parts to add? ", min_val=0)
    for _ in range(n):
        name = input_non_empty("Part name: ")
        qty = input_int("Quantity: ", min_val=1)
        price = input_float("Unit price: ₹", min_val=0.0)
        line_total = qty * price
        order["parts"].append({
            "name": name,
            "qty": qty,
            "unit_price": price,
            "line_total": line_total,
        })
    if n == 0:
        print("(No parts added)")

def compute_totals(order: Dict[str, Any]) -> None:
    parts_total = sum(p["line_total"] for p in order["parts"]) if order["parts"] else 0.0
    repair_fee = order.get("repair_fee", 0.0)
    subtotal = parts_total + repair_fee
    tax_amount = subtotal * (order.get("tax_percent", 0.0) / 100.0)
    discount_amount = subtotal * (order.get("discount_percent", 0.0) / 100.0)
    grand_total = max(0.0, subtotal + tax_amount - discount_amount)

    order["totals"].update({
        "parts_total": round(parts_total, 2),
        "subtotal": round(subtotal, 2),
        "tax_amount": round(tax_amount, 2),
        "discount_amount": round(discount_amount, 2),
        "grand_total": round(grand_total, 2),
    })

def print_invoice(order: Dict[str, Any]) -> None:
    t = order["totals"]
    print("\n================= INVOICE =================")
    print(f"Invoice No: {order['invoice_no']}")
    print(f"Date: {now_date_str()}")
    print("------------------------------------------")
    print(f"Customer: {order['customer']}")
    print(f"Device  : {order['device']}")
    print(f"Issue   : {order['issue']}")
    print(f"Due Date: {order['due_date']}")
    print("------------------------------------------")
    print("Parts:")
    if order["parts"]:
        for p in order["parts"]:
            print(
                f"  - {p['name']}  x{p['qty']}  @ {money(p['unit_price'])}  = {money(p['line_total'])}"
            )
    else:
        print("  (No parts)")
    print("------------------------------------------")
    print(f"Parts Total     : {money(t['parts_total'])}")
    print(f"Repair Fee      : {money(order['repair_fee'])}")
    print(f"Subtotal        : {money(t['subtotal'])}")
    print(f"Tax ({order['tax_percent']}%)   : {money(t['tax_amount'])}")
    print(f"Discount ({order['discount_percent']}%) : -{money(t['discount_amount'])}")
    print("------------------------------------------")
    print(f"GRAND TOTAL     : {money(t['grand_total'])}")
    print("==========================================\n")

def complete_and_bill() -> None:
    if not ORDERS:
        print("\n(No orders yet)")
        return
    oid = input_int("Enter Order ID to complete & bill: ")
    order = find_order_by_id(oid)
    if not order:
        print("❌ Order not found.")
        return
    if order["status"] == "Completed":
        print("ℹ️ This order is already completed. You can reprint the invoice.")

    choice = input("Add/Update parts before billing? (y/n): ").strip().lower()
    if choice == 'y':
        order["parts"].clear()
        add_parts_flow(order)

    order["repair_fee"] = input_float("Repair service fee (₹): ", min_val=0.0)
    order["tax_percent"] = input_float("Tax % (e.g., 18): ", min_val=0.0)
    order["discount_percent"] = input_float("Discount % (optional, can be 0): ", min_val=0.0)

    compute_totals(order)

    order["status"] = "Completed"
    order["completed_at"] = now_date_str()
    order["invoice_no"] = f"INV-{dt.datetime.now().strftime('%Y%m%d')}-{order['id']}"

    print_invoice(order)

def reprint_invoice() -> None:
    if not ORDERS:
        print("\n(No orders yet)")
        return
    oid = input_int("Order ID for invoice reprint: ")
    order = find_order_by_id(oid)
    if not order:
        print("❌ Order not found.")
        return
    if order["status"] != "Completed":
        print("ℹ️ This order is not completed yet. Complete billing first.")
        return
    compute_totals(order)
    print_invoice(order)

# ---------------------------
# Menu & App Loop
# ---------------------------

def show_menu() -> None:
    print("""
=====================================
 TechFix Solutions — FixTrack Console
=====================================
1) New repair order
2) List all orders
3) List pending orders only
4) Search orders
5) Complete & generate bill
6) Reprint invoice
0) Exit
""")

def main() -> None:
    print("👋 Welcome to FixTrack! (Console Edition)")
    while True:
        show_menu()
        choice = input("Choose option: ").strip()
        if choice == '1':
            add_order()
        elif choice == '2':
            list_orders(show_all=True)
        elif choice == '3':
            list_orders(show_all=False)
        elif choice == '4':
            search_orders()
        elif choice == '5':
            complete_and_bill()
        elif choice == '6':
            reprint_invoice()
        elif choice == '0':
            print("👋 Bye! Thanks for using FixTrack.")
            break
        else:
            print("❗ Please choose a valid option (0-6).")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n⚠️ Program interrupted. Exiting…")
