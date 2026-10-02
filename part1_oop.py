import json


class Person:
    def __init__(self, name, age, email):
        self.name = name

        if age < 0:
            raise ValueError("Age can't be negative.")

        self.age = age

        if "@" not in email or "." not in email:
            raise ValueError("Invalid email format.")

        self._email = email

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."


class Student(Person):
    def __init__(self, name, age, email, student_id):
        super().__init__(name, age, email)
        self.student_id = student_id
        self.registered_courses = []

    def register_course(self, course):
        if course not in self.registered_courses:
            self.registered_courses.append(course)

        if self not in course.enrolled_students:
            course.enrolled_students.append(self)


class Instructor(Person):
    def __init__(self, name, age, email, instructor_id):
        super().__init__(name, age, email)
        self.instructor_id = instructor_id
        self.assigned_courses = []

    def assign_course(self, course):
        if course not in self.assigned_courses:
            self.assigned_courses.append(course)


class Course:
    def __init__(self, course_id, course_name, instructor=None):
        self.course_id = course_id
        self.course_name = course_name
        self.instructor = instructor
        self.enrolled_students = []

    def add_student(self, student):
        if student not in self.enrolled_students:
            self.enrolled_students.append(student)

        if self not in student.registered_courses:
            student.registered_courses.append(self)


def save_data(students, instructors, courses):
    data = {
        "students": [],
        "instructors": [],
        "courses": []
    }

    for student in students:
        data["students"].append({
            "name": student.name,
            "age": student.age,
            "email": student._email,
            "student_id": student.student_id,
            "registered_courses": [
                course.course_id
                for course in student.registered_courses
            ]
        })

    for instructor in instructors:
        data["instructors"].append({
            "name": instructor.name,
            "age": instructor.age,
            "email": instructor._email,
            "instructor_id": instructor.instructor_id,
            "assigned_courses": [
                course.course_id
                for course in instructor.assigned_courses
            ]
        })

    for course in courses:
        instructor_id = None

        if course.instructor is not None:
            instructor_id = course.instructor.instructor_id

        data["courses"].append({
            "course_id": course.course_id,
            "course_name": course.course_name,
            "instructor_id": instructor_id,
            "enrolled_students": [
                student.student_id
                for student in course.enrolled_students
            ]
        })

    with open("school_data.json", "w") as file:
        json.dump(data, file, indent=4)


def load_data():
    with open("school_data.json", "r") as file:
        data = json.load(file)

    students = []
    instructors = []
    courses = []

    for instructor_data in data["instructors"]:
        instructor = Instructor(
            instructor_data["name"],
            instructor_data["age"],
            instructor_data["email"],
            instructor_data["instructor_id"]
        )

        instructors.append(instructor)

    for student_data in data["students"]:
        student = Student(
            student_data["name"],
            student_data["age"],
            student_data["email"],
            student_data["student_id"]
        )

        students.append(student)

    for course_data in data["courses"]:
        selected_instructor = None

        for instructor in instructors:
            if instructor.instructor_id == course_data["instructor_id"]:
                selected_instructor = instructor
                break

        course = Course(
            course_data["course_id"],
            course_data["course_name"],
            selected_instructor
        )

        courses.append(course)

        if selected_instructor is not None:
            selected_instructor.assign_course(course)

    for student_data in data["students"]:
        selected_student = None

        for student in students:
            if student.student_id == student_data["student_id"]:
                selected_student = student
                break

        for course_id in student_data["registered_courses"]:
            for course in courses:
                if course.course_id == course_id:
                    selected_student.register_course(course)
                    break

    return students, instructors, courses

