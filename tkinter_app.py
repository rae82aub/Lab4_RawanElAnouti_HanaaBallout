import tkinter as tk
from tkinter import ttk, messagebox
import json

class Person:
    """
    Represents a person in the school management system.
    """

    def __init__(self, name, age, email):
        """
        Initializes a Person object.

        :param name: Name of the person
        :type name: str
        :param age: Age of the person
        :type age: int
        :param email: Email address of the person
        :type email: str
        :raises ValueError: If the age is negative or the email format is invalid
        """

        if age < 0:
            raise ValueError("Age cannot be negative")

        if "@" not in email:
            raise ValueError("Invalid email format")

        self.name = name
        self.age = age
        self._email = email

    def introduce(self):
        """
        Returns an introduction containing the person's name and age.

        :return: Introduction of the person
        :rtype: str
        """
        return f"My name is {self.name} and I am {self.age} years old."


class Student(Person):
    """
    Represents a student in the school management system.
    """

    def __init__(self, name, age, email, student_id):
        """
        Initializes a Student object.

        :param name: Name of the student
        :type name: str
        :param age: Age of the student
        :type age: int
        :param email: Email address of the student
        :type email: str
        :param student_id: Student identification number
        :type student_id: str
        """
        super().__init__(name, age, email)

        self.student_id = student_id
        self.registered_courses = []

    def register_course(self, course):
        """
        Registers the student in a course.

        :param course: Course to register
        :type course: Course
        """

        if course not in self.registered_courses:
            self.registered_courses.append(course)


class Instructor(Person):
    """
    Represents an instructor in the school management system.
    """

    def __init__(self, name, age, email, instructor_id):
        """
        Initializes an Instructor object.

        :param name: Name of the instructor
        :type name: str
        :param age: Age of the instructor
        :type age: int
        :param email: Email address of the instructor
        :type email: str
        :param instructor_id: Instructor identification number
        :type instructor_id: str
        """
        super().__init__(name, age, email)

        self.instructor_id = instructor_id
        self.assigned_courses = []

    def assign_course(self, course):
        """
        Assigns a course to the instructor.

        :param course: Course to assign
        :type course: Course
        """

        if course not in self.assigned_courses:
            self.assigned_courses.append(course)


class Course:
    """
    Represents a course in the school management system.
    """

    def __init__(self, course_id, course_name):
        """
        Initializes a Course object.

        :param course_id: Course identification number
        :type course_id: str
        :param course_name: Name of the course
        :type course_name: str
        """
        self.course_id = course_id
        self.course_name = course_name
        self.instructor = None
        self.enrolled_students = []

    def add_student(self, student):
        """
        Adds a student to the course.

        :param student: Student to add
        :type student: Student
        """

        if student not in self.enrolled_students:
            self.enrolled_students.append(student)

students = []
instructors = []
courses = []


def find_student(student_id):
    """
    Finds a student by student ID.

    :param student_id: Student identification number
    :type student_id: str
    :return: Matching student or None
    :rtype: Student or None
    """

    for student in students:

        if student.student_id == student_id:
            return student

    return None


def find_instructor(instructor_id):
    """
    Finds an instructor by instructor ID.

    :param instructor_id: Instructor identification number
    :type instructor_id: str
    :return: Matching instructor or None
    :rtype: Instructor or None
    """
    for instructor in instructors:

        if instructor.instructor_id == instructor_id:
            return instructor

    return None


def find_course(course_id):
    """
    Finds a course by course ID.

    :param course_id: Course identification number
    :type course_id: str
    :return: Matching course or None
    :rtype: Course or None
    """
    for course in courses:

        if course.course_id == course_id:
            return course

    return None



def add_student():
    """
    Adds a new student using the values entered in the GUI.
    """
    name = student_name_entry.get()
    age = student_age_entry.get()
    email = student_email_entry.get()
    student_id = student_id_entry.get()

    if name == "" or age == "" or email == "" or student_id == "":
        messagebox.showerror(
            "Error",
            "Please fill all student fields."
        )
        return

    try:
        age = int(age)

    except ValueError:
        messagebox.showerror(
            "Error",
            "Age must be a number."
        )
        return

    if find_student(student_id) is not None:
        messagebox.showerror(
            "Error",
            "Student ID already exists."
        )
        return

    try:

        student = Student(
            name,
            age,
            email,
            student_id
        )

    except ValueError as error:

        messagebox.showerror(
            "Error",
            str(error)
        )

        return

    students.append(student)

    student_name_entry.delete(0, tk.END)
    student_age_entry.delete(0, tk.END)
    student_email_entry.delete(0, tk.END)
    student_id_entry.delete(0, tk.END)

    refresh_tree()
    refresh_dropdowns()

    messagebox.showinfo(
        "Success",
        "Student added successfully."
    )


def add_instructor():
    """
    Adds a new instructor using the values entered in the GUI.
    """
    name = instructor_name_entry.get()
    age = instructor_age_entry.get()
    email = instructor_email_entry.get()
    instructor_id = instructor_id_entry.get()

    if (
        name == ""
        or age == ""
        or email == ""
        or instructor_id == ""
    ):
        messagebox.showerror(
            "Error",
            "Please fill all instructor fields."
        )
        return

    try:
        age = int(age)

    except ValueError:
        messagebox.showerror(
            "Error",
            "Age must be a number."
        )
        return

    if find_instructor(instructor_id) is not None:

        messagebox.showerror(
            "Error",
            "Instructor ID already exists."
        )

        return

    try:

        instructor = Instructor(
            name,
            age,
            email,
            instructor_id
        )

    except ValueError as error:

        messagebox.showerror(
            "Error",
            str(error)
        )

        return

    instructors.append(instructor)

    instructor_name_entry.delete(0, tk.END)
    instructor_age_entry.delete(0, tk.END)
    instructor_email_entry.delete(0, tk.END)
    instructor_id_entry.delete(0, tk.END)

    refresh_tree()
    refresh_dropdowns()

    messagebox.showinfo(
        "Success",
        "Instructor added successfully."
    )

def add_course():
    """
    Adds a new course using the values entered in the GUI.
    """
    course_id = course_id_entry.get()
    course_name = course_name_entry.get()

    if course_id == "" or course_name == "":

        messagebox.showerror(
            "Error",
            "Please fill all course fields."
        )

        return

    if find_course(course_id) is not None:

        messagebox.showerror(
            "Error",
            "Course ID already exists."
        )

        return

    course = Course(
        course_id,
        course_name
    )

    courses.append(course)

    course_id_entry.delete(0, tk.END)
    course_name_entry.delete(0, tk.END)

    refresh_tree()
    refresh_dropdowns()

    messagebox.showinfo(
        "Success",
        "Course added successfully."
    )

def refresh_dropdowns():
    """
    Updates the student, instructor, and course dropdown lists.
    """
    student_values = []

    for student in students:

        student_values.append(
            student.student_id + " - " + student.name
        )

    instructor_values = []

    for instructor in instructors:

        instructor_values.append(
            instructor.instructor_id
            + " - "
            + instructor.name
        )

    course_values = []

    for course in courses:

        course_values.append(
            course.course_id
            + " - "
            + course.course_name
        )

    student_combo["values"] = student_values

    registration_course_combo["values"] = course_values

    instructor_combo["values"] = instructor_values

    instructor_course_combo["values"] = course_values

def register_student():
    """
    Registers the selected student in the selected course.
    """
    student_value = student_combo.get()
    course_value = registration_course_combo.get()

    if student_value == "" or course_value == "":

        messagebox.showerror(
            "Error",
            "Select a student and a course."
        )

        return

    student_id = student_value.split(" - ")[0]
    course_id = course_value.split(" - ")[0]

    student = find_student(student_id)
    course = find_course(course_id)

    if course in student.registered_courses:

        messagebox.showerror(
            "Error",
            "Student is already registered in this course."
        )

        return

    student.register_course(course)
    course.add_student(student)

    refresh_tree()

    messagebox.showinfo(
        "Success",
        "Student registered successfully."
    )

def assign_instructor():
    """
    Assigns the selected instructor to the selected course.
    """
    instructor_value = instructor_combo.get()
    course_value = instructor_course_combo.get()

    if instructor_value == "" or course_value == "":

        messagebox.showerror(
            "Error",
            "Select an instructor and a course."
        )

        return

    instructor_id = instructor_value.split(" - ")[0]
    course_id = course_value.split(" - ")[0]

    instructor = find_instructor(instructor_id)
    course = find_course(course_id)

    if course.instructor is not None:

        old_instructor = course.instructor

        if course in old_instructor.assigned_courses:
            old_instructor.assigned_courses.remove(course)

    instructor.assign_course(course)

    course.instructor = instructor

    refresh_tree()

    messagebox.showinfo(
        "Success",
        "Instructor assigned successfully."
    )

def refresh_tree():
    """
    Refreshes the records displayed in the Tkinter tree view.
    """
    search_text = search_entry.get().lower()

    for item in tree.get_children():
        tree.delete(item)

    # Students

    for student in students:

        course_names = []

        for course in student.registered_courses:
            course_names.append(course.course_name)

        courses_text = ", ".join(course_names)

        search_data = (
            student.name
            + student.student_id
            + courses_text
        ).lower()

        if search_text in search_data:

            tree.insert(
                "",
                "end",
                values=(
                    "Student",
                    student.student_id,
                    student.name,
                    courses_text
                )
            )


    for instructor in instructors:

        course_names = []

        for course in instructor.assigned_courses:
            course_names.append(course.course_name)

        courses_text = ", ".join(course_names)

        search_data = (
            instructor.name
            + instructor.instructor_id
            + courses_text
        ).lower()

        if search_text in search_data:

            tree.insert(
                "",
                "end",
                values=(
                    "Instructor",
                    instructor.instructor_id,
                    instructor.name,
                    courses_text
                )
            )


    for course in courses:

        if course.instructor is None:
            instructor_name = "Not Assigned"

        else:
            instructor_name = course.instructor.name

        student_names = []

        for student in course.enrolled_students:
            student_names.append(student.name)

        students_text = ", ".join(student_names)

        details = (
            "Instructor: "
            + instructor_name
            + " | Students: "
            + students_text
        )

        search_data = (
            course.course_id
            + course.course_name
            + instructor_name
            + students_text
        ).lower()

        if search_text in search_data:

            tree.insert(
                "",
                "end",
                values=(
                    "Course",
                    course.course_id,
                    course.course_name,
                    details
                )
            )

def delete_selected():
    """
    Deletes the selected student, instructor, or course record.
    """
    selected = tree.selection()

    if not selected:

        messagebox.showerror(
            "Error",
            "Select a record first."
        )

        return

    values = tree.item(
        selected[0],
        "values"
    )

    record_type = values[0]
    record_id = values[1]

    answer = messagebox.askyesno(
        "Delete",
        "Are you sure you want to delete this record?"
    )

    if not answer:
        return

    if record_type == "Student":

        student = find_student(record_id)

        for course in courses:

            if student in course.enrolled_students:
                course.enrolled_students.remove(student)

        students.remove(student)

    elif record_type == "Instructor":

        instructor = find_instructor(record_id)

        for course in courses:

            if course.instructor == instructor:
                course.instructor = None

        instructors.remove(instructor)

    elif record_type == "Course":

        course = find_course(record_id)

        for student in students:

            if course in student.registered_courses:
                student.registered_courses.remove(course)

        for instructor in instructors:

            if course in instructor.assigned_courses:
                instructor.assigned_courses.remove(course)

        courses.remove(course)

    refresh_tree()
    refresh_dropdowns()

def edit_selected():
    """
    Opens an edit window for the selected record.
    """
    selected = tree.selection()

    if not selected:

        messagebox.showerror(
            "Error",
            "Select a record first."
        )

        return

    values = tree.item(
        selected[0],
        "values"
    )

    record_type = values[0]
    record_id = values[1]

    edit_window = tk.Toplevel(root)

    edit_window.title("Edit " + record_type)

    edit_window.geometry("400x300")


    # STUDENT
    if record_type == "Student":

        student = find_student(record_id)

        tk.Label(
            edit_window,
            text="Name"
        ).pack()

        name_entry = tk.Entry(edit_window)
        name_entry.pack()
        name_entry.insert(0, student.name)

        tk.Label(
            edit_window,
            text="Age"
        ).pack()

        age_entry = tk.Entry(edit_window)
        age_entry.pack()
        age_entry.insert(0, student.age)

        tk.Label(
            edit_window,
            text="Email"
        ).pack()

        email_entry = tk.Entry(edit_window)
        email_entry.pack()
        email_entry.insert(0, student._email)

        def save_student_edit():

            try:
                age = int(age_entry.get())

                if age < 0:
                    raise ValueError

            except ValueError:

                messagebox.showerror(
                    "Error",
                    "Invalid age."
                )

                return

            if "@" not in email_entry.get():

                messagebox.showerror(
                    "Error",
                    "Invalid email."
                )

                return

            student.name = name_entry.get()
            student.age = age
            student._email = email_entry.get()

            refresh_tree()
            refresh_dropdowns()

            edit_window.destroy()

        tk.Button(
            edit_window,
            text="Save",
            command=save_student_edit
        ).pack(pady=10)

    elif record_type == "Instructor":

        instructor = find_instructor(record_id)

        tk.Label(
            edit_window,
            text="Name"
        ).pack()

        name_entry = tk.Entry(edit_window)
        name_entry.pack()
        name_entry.insert(0, instructor.name)

        tk.Label(
            edit_window,
            text="Age"
        ).pack()

        age_entry = tk.Entry(edit_window)
        age_entry.pack()
        age_entry.insert(0, instructor.age)

        tk.Label(
            edit_window,
            text="Email"
        ).pack()

        email_entry = tk.Entry(edit_window)
        email_entry.pack()
        email_entry.insert(0, instructor._email)

        def save_instructor_edit():

            try:

                age = int(age_entry.get())

                if age < 0:
                    raise ValueError

            except ValueError:

                messagebox.showerror(
                    "Error",
                    "Invalid age."
                )

                return

            if "@" not in email_entry.get():

                messagebox.showerror(
                    "Error",
                    "Invalid email."
                )

                return

            instructor.name = name_entry.get()
            instructor.age = age
            instructor._email = email_entry.get()

            refresh_tree()
            refresh_dropdowns()

            edit_window.destroy()

        tk.Button(
            edit_window,
            text="Save",
            command=save_instructor_edit
        ).pack(pady=10)


    # COURSE
    elif record_type == "Course":

        course = find_course(record_id)

        tk.Label(
            edit_window,
            text="Course Name"
        ).pack()

        course_name_entry_edit = tk.Entry(edit_window)

        course_name_entry_edit.pack()

        course_name_entry_edit.insert(
            0,
            course.course_name
        )

        def save_course_edit():

            course.course_name = (
                course_name_entry_edit.get()
            )

            refresh_tree()
            refresh_dropdowns()

            edit_window.destroy()

        tk.Button(
            edit_window,
            text="Save",
            command=save_course_edit
        ).pack(pady=10)



def save_data():
    """
    Saves the current school management data to a JSON file.
    """
    data = {
        "students": [],
        "instructors": [],
        "courses": []
    }

    for student in students:

        registered_courses = []

        for course in student.registered_courses:
            registered_courses.append(course.course_id)

        data["students"].append(
            {
                "name": student.name,
                "age": student.age,
                "email": student._email,
                "student_id": student.student_id,
                "registered_courses": registered_courses
            }
        )


    for instructor in instructors:

        assigned_courses = []

        for course in instructor.assigned_courses:
            assigned_courses.append(course.course_id)

        data["instructors"].append(
            {
                "name": instructor.name,
                "age": instructor.age,
                "email": instructor._email,
                "instructor_id": instructor.instructor_id,
                "assigned_courses": assigned_courses
            }
        )


    for course in courses:

        student_ids = []

        for student in course.enrolled_students:
            student_ids.append(student.student_id)

        if course.instructor is None:
            instructor_id = None

        else:
            instructor_id = course.instructor.instructor_id

        data["courses"].append(
            {
                "course_id": course.course_id,
                "course_name": course.course_name,
                "instructor": instructor_id,
                "students": student_ids
            }
        )


    with open(
        "school_data.json",
        "w"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )

    messagebox.showinfo(
        "Success",
        "Data saved successfully."
    )

def load_data():
    """
    Loads school management data from a JSON file.
    """
    try:

        with open(
            "school_data.json",
            "r"
        ) as file:

            data = json.load(file)

    except FileNotFoundError:

        messagebox.showerror(
            "Error",
            "No saved file found."
        )

        return


    students.clear()
    instructors.clear()
    courses.clear()


    for item in data["students"]:

        student = Student(
            item["name"],
            item["age"],
            item["email"],
            item["student_id"]
        )

        students.append(student)
    for item in data["instructors"]:

        instructor = Instructor(
            item["name"],
            item["age"],
            item["email"],
            item["instructor_id"]
        )

        instructors.append(instructor)



    for item in data["courses"]:

        course = Course(
            item["course_id"],
            item["course_name"]
        )

        courses.append(course)


    for item in data["students"]:

        student = find_student(
            item["student_id"]
        )

        for course_id in item["registered_courses"]:

            course = find_course(course_id)

            if course is not None:

                student.register_course(course)

                course.add_student(student)


    # Restore instructor assignments

    for item in data["instructors"]:

        instructor = find_instructor(
            item["instructor_id"]
        )

        for course_id in item["assigned_courses"]:

            course = find_course(course_id)

            if course is not None:

                instructor.assign_course(course)

                course.instructor = instructor


    refresh_tree()
    refresh_dropdowns()

    messagebox.showinfo(
        "Success",
        "Data loaded successfully."
    )


if __name__ == "__main__":
    root = tk.Tk()

    root.title(
        "School Management System"
    )

    root.geometry(
        "1100x750"
    )


    title_label = tk.Label(
        root,
        text="School Management System",
        font=("Arial", 20)
    )

    title_label.pack(
        pady=10
    )


    notebook = ttk.Notebook(root)

    notebook.pack(
        fill="x",
        padx=20,
        pady=5
    )


    student_frame = ttk.Frame(notebook)

    instructor_frame = ttk.Frame(notebook)

    course_frame = ttk.Frame(notebook)

    registration_frame = ttk.Frame(notebook)


    notebook.add(
        student_frame,
        text="Student"
    )

    notebook.add(
        instructor_frame,
        text="Instructor"
    )

    notebook.add(
        course_frame,
        text="Course"
    )

    notebook.add(
        registration_frame,
        text="Registration / Assignment"
    )

    tk.Label(
        student_frame,
        text="Name"
    ).grid(
        row=0,
        column=0,
        padx=10,
        pady=10
    )

    student_name_entry = tk.Entry(
        student_frame
    )

    student_name_entry.grid(
        row=0,
        column=1
    )


    tk.Label(
        student_frame,
        text="Age"
    ).grid(
        row=0,
        column=2,
        padx=10
    )

    student_age_entry = tk.Entry(
        student_frame
    )

    student_age_entry.grid(
        row=0,
        column=3
    )


    tk.Label(
        student_frame,
        text="Email"
    ).grid(
        row=1,
        column=0,
        padx=10,
        pady=10
    )

    student_email_entry = tk.Entry(
        student_frame
    )

    student_email_entry.grid(
        row=1,
        column=1
    )


    tk.Label(
        student_frame,
        text="Student ID"
    ).grid(
        row=1,
        column=2,
        padx=10
    )

    student_id_entry = tk.Entry(
        student_frame
    )

    student_id_entry.grid(
        row=1,
        column=3
    )


    tk.Button(
        student_frame,
        text="Add Student",
        command=add_student
    ).grid(
        row=2,
        column=1,
        pady=10
    )




    tk.Label(
        instructor_frame,
        text="Name"
    ).grid(
        row=0,
        column=0,
        padx=10,
        pady=10
    )

    instructor_name_entry = tk.Entry(
        instructor_frame
    )

    instructor_name_entry.grid(
        row=0,
        column=1
    )


    tk.Label(
        instructor_frame,
        text="Age"
    ).grid(
        row=0,
        column=2,
        padx=10
    )

    instructor_age_entry = tk.Entry(
        instructor_frame
    )

    instructor_age_entry.grid(
        row=0,
        column=3
    )


    tk.Label(
        instructor_frame,
        text="Email"
    ).grid(
        row=1,
        column=0,
        padx=10,
        pady=10
    )

    instructor_email_entry = tk.Entry(
        instructor_frame
    )

    instructor_email_entry.grid(
        row=1,
        column=1
    )


    tk.Label(
        instructor_frame,
        text="Instructor ID"
    ).grid(
        row=1,
        column=2,
        padx=10
    )

    instructor_id_entry = tk.Entry(
        instructor_frame
    )

    instructor_id_entry.grid(
        row=1,
        column=3
    )


    tk.Button(
        instructor_frame,
        text="Add Instructor",
        command=add_instructor
    ).grid(
        row=2,
        column=1,
        pady=10
    )


    tk.Label(
        course_frame,
        text="Course ID"
    ).grid(
        row=0,
        column=0,
        padx=10,
        pady=10
    )

    course_id_entry = tk.Entry(
        course_frame
    )

    course_id_entry.grid(
        row=0,
        column=1
    )


    tk.Label(
        course_frame,
        text="Course Name"
    ).grid(
        row=0,
        column=2,
        padx=10
    )

    course_name_entry = tk.Entry(
        course_frame
    )

    course_name_entry.grid(
        row=0,
        column=3
    )


    tk.Button(
        course_frame,
        text="Add Course",
        command=add_course
    ).grid(
        row=1,
        column=1,
        pady=10
    )


    tk.Label(
        registration_frame,
        text="Student"
    ).grid(
        row=0,
        column=0,
        padx=10,
        pady=10
    )

    student_combo = ttk.Combobox(
        registration_frame,
        state="readonly",
        width=30
    )

    student_combo.grid(
        row=0,
        column=1
    )


    tk.Label(
        registration_frame,
        text="Course"
    ).grid(
        row=0,
        column=2,
        padx=10
    )

    registration_course_combo = ttk.Combobox(
        registration_frame,
        state="readonly",
        width=30
    )

    registration_course_combo.grid(
        row=0,
        column=3
    )


    tk.Button(
        registration_frame,
        text="Register Student",
        command=register_student
    ).grid(
        row=0,
        column=4,
        padx=10
    )



    tk.Label(
        registration_frame,
        text="Instructor"
    ).grid(
        row=1,
        column=0,
        padx=10,
        pady=10
    )

    instructor_combo = ttk.Combobox(
        registration_frame,
        state="readonly",
        width=30
    )

    instructor_combo.grid(
        row=1,
        column=1
    )


    tk.Label(
        registration_frame,
        text="Course"
    ).grid(
        row=1,
        column=2,
        padx=10
    )

    instructor_course_combo = ttk.Combobox(
        registration_frame,
        state="readonly",
        width=30
    )

    instructor_course_combo.grid(
        row=1,
        column=3
    )


    tk.Button(
        registration_frame,
        text="Assign Instructor",
        command=assign_instructor
    ).grid(
        row=1,
        column=4,
        padx=10
    )



    search_frame = tk.Frame(root)

    search_frame.pack(
        fill="x",
        padx=20,
        pady=10
    )


    tk.Label(
        search_frame,
        text="Search:"
    ).pack(
        side="left"
    )

    search_entry = tk.Entry(
        search_frame,
        width=40
    )

    search_entry.pack(
        side="left",
        padx=10
    )


    tk.Button(
        search_frame,
        text="Search",
        command=refresh_tree
    ).pack(
        side="left"
    )


    tk.Button(
        search_frame,
        text="Clear",
        command=lambda: (
            search_entry.delete(0, tk.END),
            refresh_tree()
        )
    ).pack(
        side="left",
        padx=5
    )


    tree = ttk.Treeview(
        root,
        columns=(
            "Type",
            "ID",
            "Name",
            "Details"
        ),
        show="headings"
    )


    tree.heading(
        "Type",
        text="Type"
    )

    tree.heading(
        "ID",
        text="ID"
    )

    tree.heading(
        "Name",
        text="Name"
    )

    tree.heading(
        "Details",
        text="Details"
    )


    tree.column(
        "Type",
        width=100
    )

    tree.column(
        "ID",
        width=100
    )

    tree.column(
        "Name",
        width=180
    )

    tree.column(
        "Details",
        width=500
    )


    tree.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=10
    )


    button_frame = tk.Frame(root)

    button_frame.pack(
        pady=10
    )


    tk.Button(
        button_frame,
        text="Edit Selected",
        command=edit_selected
    ).pack(
        side="left",
        padx=5
    )


    tk.Button(
        button_frame,
        text="Delete Selected",
        command=delete_selected
    ).pack(
        side="left",
        padx=5
    )


    tk.Button(
        button_frame,
        text="Save Data",
        command=save_data
    ).pack(
        side="left",
        padx=5
    )


    tk.Button(
        button_frame,
        text="Load Data",
        command=load_data
    ).pack(
        side="left",
        padx=5
    )



    refresh_tree()

    root.mainloop()