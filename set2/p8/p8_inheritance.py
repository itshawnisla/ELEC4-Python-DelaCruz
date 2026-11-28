

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello! My name is {self.name} and I am {self.age} years old.")



class Student(Person):
    def __init__(self, name, age, student_id, course):
        super().__init__(name, age)
        self.student_id = student_id
        self.course = course

    
    def introduce(self):
        print(f"I am {self.name}, a student.")
        print(f"Age: {self.age}")
        print(f"Student ID: {self.student_id}")
        print(f"Course: {self.course}")



class Teacher(Person):
    def __init__(self, name, age, subject, years_experience):
        super().__init__(name, age)
        self.subject = subject
        self.years_experience = years_experience

    # Override introduce()
    def introduce(self):
        print(f"I am {self.name}, a teacher.")
        print(f"Age: {self.age}")
        print(f"Subject: {self.subject}")
        print(f"Years of Experience: {self.years_experience}")


def main():
    
    person1 = Student("Maria Santos", 20, "2026-001", "BSIT")
    person2 = Teacher("Mr. Dela Cruz", 35, "Programming", 10)
    person3 = Student("Juan Reyes", 21, "2026-002", "BSIT")

    
    people = [person1, person2, person3]

    
    print("===== PERSON INTRODUCTIONS =====")

    for person in people:
        person.introduce()
        print()


if __name__ == "__main__":
    main()



