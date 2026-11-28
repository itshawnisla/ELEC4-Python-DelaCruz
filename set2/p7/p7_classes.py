
# Student: Shawn Isla M. Dela Cruz | Section: IV-BSIT-A | Activity: P7 | Date: 2026-11-18


class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.__grade = grade

    def display_info(self):
        print("\nStudent ID:", self.student_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Grade:", self.get_grade())

    def update_info(self, name, age):
        self.name = name
        self.age = age
        print("Student information updated successfully!")

    def get_grade(self):
        return self.__grade

    def set_grade(self, new_grade):
        if isinstance(new_grade, (int, float)) and not isinstance(new_grade, bool) and 0 <= new_grade <= 100:
            self.__grade = new_grade
            print("Grade updated successfully!")
        else:
            print("Invalid grade. Grade must be between 0 and 100.")


class Subject:
    def __init__(self, subject_name, teacher):
        self.subject_name = subject_name
        self.teacher = teacher

    def display_subject(self):
        print("Subject:", self.subject_name)
        print("Teacher:", self.teacher)


class Section:
    def __init__(self, section_name, subject):
        self.section_name = section_name
        self.subject = subject
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_section(self):
        print("\n===== SECTION INFORMATION =====")
        print("Section:", self.section_name)
        self.subject.display_subject()

        print("\n===== STUDENT LIST =====")

        for student in self.students:
            student.display_info()


def main():
  
    subject = Subject("Programming", "Mr. Dela Cruz")

    section = Section("IV-BSIT-A", subject)

    # Create three Student objects
    student1 = Student("2026-001", "Juan Dela Cruz", 20, 90)
    student2 = Student("2026-002", "Maria Santos", 19, 85)
    student3 = Student("2026-003", "Pedro Reyes", 21, 88)

   
    section.add_student(student1)
    section.add_student(student2)
    section.add_student(student3)

    print("===== UPDATE STUDENT =====")
    student2.update_info("Maria Santos", 20)
    student2.set_grade(92)

    
    section.display_section()


if __name__ == "__main__":
    main()
