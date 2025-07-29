# Print pattern using nested for loop
for i in range(1, 6):        # Outer loop for rows
    for j in range(i):       # Inner loop for stars
        print("*", end="")   # Print stars on same line
    print()                  # Move to next line
