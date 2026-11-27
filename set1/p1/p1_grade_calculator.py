


def get_grades():
    grades = []

    for i in range(5):
        while True:
            try:
                grade = float(input("Enter grade: "))

                if 0 <= grade <= 100:
                    grades.append(grade)
                    break
                else:
                    print("Invalid grade. Please try again.")

            except ValueError:
                print("Invalid input. Please enter a number.")

    return grades


def calculate_average(grades):
    return sum(grades) / len(grades)


def get_highest(grades):
    return max(grades)


def get_lowest(grades):
    return min(grades)


def get_status(grades):
    if calculate_average(grades) >= 75:
        return "PASSED"
    else:
        return "FAILED"


def show_results(grades):
    print("\n--- GRADE REPORT ---")
    print("Grades:", grades)
    print(f"Average: {calculate_average(grades):.2f}")
    print(f"Highest: {get_highest(grades):.2f}")
    print(f"Lowest: {get_lowest(grades):.2f}")
    print(f"Status: {get_status(grades)}")


def main():
    grades = []

    while True:
        print("\nSTUDENT GRADE CALCULATOR")
        print("1. Enter grades")
        print("2. View results")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            grades = get_grades()

        elif choice == "2":
            if grades:
                show_results(grades)
            else:
                print("No grades yet. Choose option 1 first.")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid menu choice. Select 1, 2, or 3.")


if __name__ == "__main__":
    main()


