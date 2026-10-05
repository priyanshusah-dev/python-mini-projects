terms = int(input("Enter the number of terms: "))

first = 0
second = 1

if terms <= 0:
    print("Please enter a positive number.")
else:
    print("Fibonacci sequence:")

    for i in range(terms):
        print(first, end=" ")
        first, second = second, first + second
