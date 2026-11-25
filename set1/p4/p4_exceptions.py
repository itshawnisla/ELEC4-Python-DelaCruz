


def division():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        result = num1 / num2

    except ValueError:
        print("Invalid input. Please enter numbers only.")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

    else:
        print("Result:", result)

    finally:
        print("Division operation completed.")


def open_file():
    try:
        filename = input("Enter file name: ")

        file = open(filename, "r")
        contents = file.read()
        file.close()

    except FileNotFoundError:
        print("Error: File not found.")

    else:
        print("\n--- FILE CONTENTS ---")
        print(contents)

    finally:
        print("File operation completed.")


def main():
    while True:
        print("\n===== EXCEPTION HANDLING PROGRAM =====")
        print("1. Divide two numbers")
        print("2. Open a text file")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            division()

        elif choice == "2":
            open_file()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid menu selection. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
