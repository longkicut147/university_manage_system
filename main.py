class Person:
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age

class University:
    def __init__(self, name:str):
        self.name = name    # name of university
        self.faculty = []
    
    def add_faculty(self, faculty):
        if type(faculty) == Faculty:
            self.faculty.append(faculty)
        else:
            raise ValueError("faculty must be an instance")

class Faculty(University):
    def __init__(self, name:str):
        self.name = name    # name of faculty
        self.lecturer = []
        self.course = []

    def add_lecturer(self, lecturer):
        self.lecturer.append(lecturer)

    def add_course(self, course):
        self.course.append(course)

class Lecturer(Person):
    def __init__(self, name, age, faculty):
        super().__init__(name, age)
        self.faculty = faculty
        self.courses = []

    def assign_course(self, course):
        self.courses.append(course)

class Course:
    def __init__(self, name, credits, lecturer):
        self.name = name    # name of course
        self.credits = credits
        self.lecturer = lecturer
        self.students = []

    def add_student(self, student):
        self.students.append(student)

class Student(Person):
    def __init__(self, name: str, age: int, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.courses = []

    def register_course(self, course:Course):
        self.courses.append(course)
        course.add_student(self)


# Create a university object
university = University("Tech University")
# Create an IT Faculty
faculty_it = Faculty("Faculty of Information Technology")
university.add_faculty(faculty_it)
# Create lecturers
lecturer1 = Lecturer("Dr. John Smith", 40, faculty_it)
lecturer2 = Lecturer("Dr. Jane Doe", 35, faculty_it)
faculty_it.add_lecturer(lecturer1)
faculty_it.add_lecturer(lecturer2)
# Create courses
course_python = Course("Python Programming", 3, lecturer1)
course_web = Course("Web Development", 4, lecturer2)
faculty_it.add_course(course_python)
faculty_it.add_course(course_web)
# Assign lecturers to teach courses
lecturer1.assign_course(course_python)
lecturer2.assign_course(course_web)
# Create students and register them for courses
student1 = Student("Alice Johnson", 20, "ST001")
student2 = Student("Bob Williams", 21, "ST002")
student1.register_course(course_python)
student2.register_course(course_web)
# Print information about students and their registered courses
print(f"Student {student1.name} registered for {student1.courses[0].name}")
print(f"Student {student2.name} registered for {student2.courses[0].name}")
# Print information about lecturers and the courses they teach
print(f"Lecturer {lecturer1.name} teaches {lecturer1.courses[0].name}")
print(f"Lecturer {lecturer2.name} teaches {lecturer2.courses[0].name}")