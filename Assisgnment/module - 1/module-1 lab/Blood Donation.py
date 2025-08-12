# Check blood donation eligibility

age = int(input("Enter your age: "))
weight = float(input("Enter your weight (in kg): "))

if age >= 18:
    if weight >= 50:
        print("You are eligible to donate blood.")
    else:
        print("You are NOT eligible: Your weight is less than 50 kg.")
else:
    print("You are NOT eligible: Age must be 18 or above.")
