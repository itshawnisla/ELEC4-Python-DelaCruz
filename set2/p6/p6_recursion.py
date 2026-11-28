

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)



def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)



def sum_numbers(n):
    if n == 0:
        return 0
    return n + sum_numbers(n - 1)



def search(items, target):
    if len(items) == 0:
        return False
    if items[0] == target:
        return True
    return search(items[1:], target)


def display_fibonacci_terms(n):
    print("Fibonacci sequence:")

    for i in range(n):
        print(fibonacci(i), end=" ")

    print()


def main():
    while True:
        print("\n===== RECURSION PROGRAM =====")
        print("1. Factorial")
        print("2. Fibonacci")
        print("3. Sum of Numbers")
        print("4. Search in a List")
        print("5. Exit")

        choice = input("Choose: ")

        if choice == "1":
            try:
                n = int(input("Enter a non-negative number: "))

                if n < 0:
                    print("Please enter a non-negative number.")
                else:
                    print(f"Factorial of {n}: {factorial(n)}")

            except ValueError:
                print("Invalid input. Please enter an integer.")

        elif choice == "2":
            try:
                n = int(input("Enter the number of Fibonacci terms: "))

                if n < 0:
                    print("Please enter a non-negative number.")
                else:
                    display_fibonacci_terms(n)
                    if n > 0:
                        print(f"The {n}th Fibonacci number: {fibonacci(n - 1)}")

            except ValueError:
                print("Invalid input. Please enter an integer.")

        elif choice == "3":
            try:
                n = int(input("Enter a non-negative number: "))

                if n < 0:
                    print("Please enter a non-negative number.")
                else:
                    print(f"Sum from 1 to {n}: {sum_numbers(n)}")

            except ValueError:
                print("Invalid input. Please enter an integer.")

        elif choice == "4":
            items = input("Enter list items separated by spaces: ").split()
            target = input("Enter the value to search: ")

            if search(items, target):
                print("Target found!")
            else:
                print("Target not found.")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1 to 5.")


if __name__ == "__main__":
    main()
