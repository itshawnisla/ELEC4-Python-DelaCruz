


students = []


def add_student():
    name = input("Enter student name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    existing_names = {student.lower() for student in students}

    if name.lower() in existing_names:
        print("Student already exists.")
    else:
        students.append(name)
        print("Student successfully added!")


def remove_student():
    name = input("Enter student name to remove: ").strip()

    for student in students:
        if student.lower() == name.lower():
            students.remove(student)
            print("Student successfully removed!")
            return

    print("Student not found.")


def search_student():
    name = input("Enter name to search: ").strip().lower()

    if not name:
        print("Please enter a name to search.")
        return

    matches = [student for student in students if name in student.lower()]

    if matches:
        print("\n--- SEARCH RESULTS ---")
        for student in sorted(matches, key=str.lower):
            print(student)
    else:
        print("No matching student found.")


def display_students():
    print("\n--- STUDENT LIST ---")

    if not students:
        print("No students recorded.")
        print("Total students: 0")
        return

    sorted_students = sorted(students, key=str.lower)

    for number, student in enumerate(sorted_students, start=1):
        print(f"{number}. {student}")

    print("Total students:", len(students))


def main():
    while True:
        print("\n===== STUDENT RECORD MANAGER =====")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Search Student")
        print("4. Display All Students")
        print("5. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            remove_student()

        elif choice == "3":
            search_student()

        elif choice == "4":
            display_students()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1 to 5.")


if __name__ == "__main__":
    main()



