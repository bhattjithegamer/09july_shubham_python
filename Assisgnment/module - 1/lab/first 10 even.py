# Generator function to generate first 10 even numbers
def generate_even_numbers():
    num = 0
    for _ in range(10):
        yield num
        num += 2

# Using the generator
print("First 10 even numbers:")
for even in generate_even_numbers():
    print(even)
