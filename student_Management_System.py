class Student:
    #  Initializes the student object with the provided ID, name, age, and major.
    def __init__(self, id: int, name: str, age: int, major: str):
        self.id = id
        self.name = name
        self.age = age
        self.major = major

    # Updates the student's information based on the provided parameters.
    def update(self, name: str = None, age: int = None, major: str = None):
        self.name = name or self.name
        self.age = age or self.age
        self.major = major or self.major

    # Displays the student's information.
    def display(self):
        print(f"Student ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Major: {self.major}")


class StudentDatabase:
    #  Initializes an empty dictionary to store student objects.
    def __init__(self):
        self._students = {}

    # Adds a new student to the database.
    def add(self, student: Student):
        self._students[student.id] = student
    
    # Removes a student from the database base on their ID.
    def remove(self, student_id: int):
        if student_id in self._students:
            del self._students[student_id]

    # Retrieves a student from the database based on their ID.
    def get_student(self, student_id: int) -> Student:
        return self._students.get(student_id)
    
    # Displays all the students in the database.
    def display_all(self):
        for student in self._students.values():
            student.display()


class StudentManagementSystem:
    # Initializes the student management system with an empty database
    def __init__(self):
        self.database = StudentDatabase()

    # Adds a new student to the system. Already existing student IDs won't be added
    def add_new_student(self, id: int, name: str, age: int, major: str):
        student = Student(id, name, age, major)
        if id in self.database._students:
            print("Student already exists.")
        else:
            self.database.add(student)

                                                                            
    # Deletes a student from the system based on their ID.
    def delete_student(self, student_id: int):
        student = self.database.get_student(student_id)
        if student:
            print(f"{student.name} : was deleted")
            self.database.remove(student_id)
        else:
            print("Student not found.")

    # Updates a student's information in the system based on their ID.
    def update_student(self, student_id: int, name: str = None, age: int = None, major: str = None):
        student = self.database.get_student(student_id)
        if student:
            student.update(name, age, major)

    # Displays all the students in the system. "NO students in the system" will be displayed if the database has no students
    def show_all_students(self):
        if not self.database._students:
            print("No students in the system. Please add students to the database before displaying them.")
        else:
            self.database.display_all()

    # Provides a text based menu for users to interact with the system.
    def menu(self):
        while True:
            print("\nStudent Management System Menu:")
            print("1. Add Student")
            print("2. Delete Student")
            print("3. Update Student Info")
            print("4. View All Students")
            print("5. Quit")
            
            choice = input("Enter your choice (1/2/3/4/5): ")
            
            if choice == '1':
                try:
                    id_ = int(input("Enter Student ID: "))
                    name = input("Enter Student Name: ")
                    age = int(input("Enter Student Age: "))
                    major = input("Enter Student Major: ")
                    self.add_new_student(id_, name, age, major)
                except ValueError:
                    print("Invalid input! Student ID and age must be integers: name and major must be strings.")
            
            elif choice == '2':
                try:
                    id_ = int(input("Enter Student ID to delete: "))
                    self.delete_student(id_)
                except ValueError:
                    print("Invalid input! Student ID must be an integer.")
            
            elif choice == '3':
                try:
                    id_ = int(input("Enter Student ID to update: "))
                    name = input("Enter new name (or press Enter to skip): ")
                    age = input("Enter new age (or press Enter to skip): ")
                    major = input("Enter new major (or press Enter to skip): ")
                    if name.isdigit() or major.isdigit():
                        print("Invalid input! Name and major must be strings.")
                    else:
                        self.update_student(id_, name, int(age) if age.isdigit() else None, major)
                except ValueError:
                    print("Invalid input! Student ID must be an integer, and age must be an integer or left blank.")
            
            elif choice == '4':
                self.show_all_students()
            
            elif choice == '5':
                print("Exiting...")
                break
            
            else:
                print("Invalid choice! Please choose a valid option.")

system = StudentManagementSystem()
system.menu()