


FILENAME = "students.txt"


def load_records():
    records = []

    try:
        with open(FILENAME, "r") as file:
            for line in file:
                parts = line.strip().split("|")

                if len(parts) == 4:
                    try:
                        record = {
                            "id": parts[0],
                            "name": parts[1],
                            "course": parts[2],
                            "average": float(parts[3])
                        }
                        records.append(record)
                    except ValueError:
                        print("A record with invalid average was skipped.")

    except FileNotFoundError:
        print("No existing records found. Starting with an empty list.")

    return records


def save_records(records):
    with open(FILENAME, "w") as file:
        for student in records:
            file.write(
                f"{student['id']}|{student['name']}|"
                f"{student['course']}|{student['average']}\n"
            )


def read_average():
    while True:
        try:
            average = float(input("Enter general average: "))

            if 0 <= average <= 100:
                return average
            else:
                print("Average must be between 0 and 100.")

        except ValueError:
            print("Invalid input. Please enter a number.")


def add_student(records):
    print("\n--- ADD STUDENT ---")

    student_id = input("Enter student ID: ").strip()

    if not student_id:
        print("Student ID cannot be empty.")
        return

    if any(student["id"].lower() == student_id.lower() for student in records):
        print("Student ID already exists.")
        return

    name = input("Enter full name: ").strip()
    course = input("Enter course/section: ").strip()

    if not name or not course:
        print("Name and course/section cannot be empty.")
        return

    if "|" in student_id or "|" in name or "|" in course:
        print("The | character is not allowed.")
        return

    average = read_average()

    student = {
        "id": student_id,
        "name": name,
        "course": course,
        "average": average
    }

    records.append(student)
    save_records(records)

    print("Student record successfully added!")


def display_students(records):
    print("\n--- ALL STUDENT RECORDS ---")

    if not records:
        print("No student records available.")
        return

    for number, student in enumerate(records, start=1):
        print(f"\nStudent #{number}")
        print("Student ID:", student["id"])
        print("Full Name:", student["name"])
        print("Course/Section:", student["course"])
        print(f"General Average: {student['average']:.2f}")

    print("\nTotal students:", len(records))


def search_student(records):
    print("\n--- SEARCH STUDENT ---")

    student_id = input("Enter student ID to search: ").strip()

    for student in records:
        if student["id"].lower() == student_id.lower():
            print("\nStudent Found!")
            print("Student ID:", student["id"])
            print("Full Name:", student["name"])
            print("Course/Section:", student["course"])
            print(f"General Average: {student['average']:.2f}")
            return

    print("Student record not found.")


def update_student(records):
    print("\n--- UPDATE STUDENT ---")

    student_id = input("Enter student ID to update: ").strip()

    for student in records:
        if student["id"].lower() == student_id.lower():

            print("\nStudent Found!")
            print("Leave a field blank to keep its current information.")

            new_id = input("Enter new student ID: ").strip()
            new_name = input("Enter new full name: ").strip()
            new_course = input("Enter new course/section: ").strip()

            if new_id and "|" in new_id:
                print("The | character is not allowed.")
                return

            if new_name and "|" in new_name:
                print("The | character is not allowed.")
                return

            if new_course and "|" in new_course:
                print("The | character is not allowed.")
                return

            if new_id:
                duplicate = any(
                    other["id"].lower() == new_id.lower()
                    for other in records
                    if other is not student
                )

                if duplicate:
                    print("That student ID already exists.")
                    return

                student["id"] = new_id

            if new_name:
                student["name"] = new_name

            if new_course:
                student["course"] = new_course

            while True:
                change_average = input(
                    "Update general average? (y/n): "
                ).strip().lower()

                if change_average == "y":
                    student["average"] = read_average()
                    break
                elif change_average == "n":
                    break
                else:
                    print("Please enter y or n.")

            save_records(records)
            print("Student record successfully updated!")
            return

    print("Student record not found.")


def main():
    records = load_records()

    while True:
        print("\n===== STUDENT RECORD SYSTEM =====")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student by ID")
        print("4. Update Student Information")
        print("5. Exit")

        choice = input("Choose: ").strip()

        if choice == "1":
            add_student(records)

        elif choice == "2":
            display_students(records)

        elif choice == "3":
            search_student(records)

        elif choice == "4":
            update_student(records)

        elif choice == "5":
            print("Records saved successfully.")
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1 to 5.")


if __name__ == "__main__":
    main()
