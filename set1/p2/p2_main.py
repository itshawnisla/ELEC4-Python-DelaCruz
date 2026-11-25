


import student_utils
from student_utils import calculate_average, get_status
from datetime import datetime


def read_grades():
    grades = []

    while len(grades) < 5:
        try:
            grade = float(input("Enter grade: "))

            if 0 <= grade <= 100:
                grades.append(grade)
            else:
                print("Invalid grade. Please try again.")

        except ValueError:
            print("Invalid input. Please enter a number.")

    return grades


def main():
    print("STUDENT REPORT")

    grades = read_grades()

    print("\n--- STUDENT GRADE REPORT ---")
    print("Generated:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    print(f"Average: {calculate_average(grades):.2f}")
    print("Highest:", student_utils.get_highest(grades))
    print("Lowest:", student_utils.get_lowest(grades))
    print("Status:", get_status(grades))


if __name__ == "__main__":
    main()
