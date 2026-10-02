import sys
import json
import csv

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QComboBox,
    QTableWidget,
    QTableWidgetItem,
    QMessageBox,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QGroupBox,
    QFileDialog,
    QInputDialog
)

from part1_oop import Person, Student, Instructor, Course


students = []
instructors = []
courses = []


class SchoolManagementSystem(QWidget):
    """Provide the PyQt5 interface for managing school records.

    The interface supports adding students, instructors, and courses,
    registering students in courses, searching records, editing and deleting
    records, saving and loading JSON data, and exporting records to CSV.
    """

    def __init__(self):
        """Initialize the main window and create all GUI sections.

        :return: None
        :rtype: None
        """
        super().__init__()

        self.setWindowTitle("School Management System")
        self.resize(1000, 800)

        self.main_layout = QVBoxLayout()

        self.create_student_section()
        self.create_instructor_section()
        self.create_course_section()
        self.create_registration_section()
        self.create_search_section()
        self.create_table()
        self.create_action_buttons()

        self.setLayout(self.main_layout)

    def create_student_section(self):
        """Create the section used to enter and add student information.

        :return: None
        :rtype: None
        """
        group = QGroupBox("Add Student")
        layout = QGridLayout()

        self.student_name = QLineEdit()
        self.student_age = QLineEdit()
        self.student_email = QLineEdit()
        self.student_id = QLineEdit()

        layout.addWidget(QLabel("Name:"), 0, 0)
        layout.addWidget(self.student_name, 0, 1)

        layout.addWidget(QLabel("Age:"), 1, 0)
        layout.addWidget(self.student_age, 1, 1)

        layout.addWidget(QLabel("Email:"), 2, 0)
        layout.addWidget(self.student_email, 2, 1)

        layout.addWidget(QLabel("Student ID:"), 3, 0)
        layout.addWidget(self.student_id, 3, 1)

        button = QPushButton("Add Student")
        button.clicked.connect(self.add_student)

        layout.addWidget(button, 4, 0, 1, 2)

        group.setLayout(layout)
        self.main_layout.addWidget(group)

    def create_instructor_section(self):
        """Create the section used to enter and add instructor information.

        :return: None
        :rtype: None
        """
        group = QGroupBox("Add Instructor")
        layout = QGridLayout()

        self.instructor_name = QLineEdit()
        self.instructor_age = QLineEdit()
        self.instructor_email = QLineEdit()
        self.instructor_id = QLineEdit()

        layout.addWidget(QLabel("Name:"), 0, 0)
        layout.addWidget(self.instructor_name, 0, 1)

        layout.addWidget(QLabel("Age:"), 1, 0)
        layout.addWidget(self.instructor_age, 1, 1)

        layout.addWidget(QLabel("Email:"), 2, 0)
        layout.addWidget(self.instructor_email, 2, 1)

        layout.addWidget(QLabel("Instructor ID:"), 3, 0)
        layout.addWidget(self.instructor_id, 3, 1)

        button = QPushButton("Add Instructor")
        button.clicked.connect(self.add_instructor)

        layout.addWidget(button, 4, 0, 1, 2)

        group.setLayout(layout)
        self.main_layout.addWidget(group)

    def create_course_section(self):
        """Create the section used to enter and add course information.

        :return: None
        :rtype: None
        """
        group = QGroupBox("Add Course")
        layout = QGridLayout()

        self.course_id = QLineEdit()
        self.course_name = QLineEdit()
        self.course_instructor = QComboBox()

        layout.addWidget(QLabel("Course ID:"), 0, 0)
        layout.addWidget(self.course_id, 0, 1)

        layout.addWidget(QLabel("Course Name:"), 1, 0)
        layout.addWidget(self.course_name, 1, 1)

        layout.addWidget(QLabel("Instructor:"), 2, 0)
        layout.addWidget(self.course_instructor, 2, 1)

        button = QPushButton("Add Course")
        button.clicked.connect(self.add_course)

        layout.addWidget(button, 3, 0, 1, 2)

        group.setLayout(layout)
        self.main_layout.addWidget(group)

    def create_registration_section(self):
        """Create the section used to register a student in a course.

        :return: None
        :rtype: None
        """
        group = QGroupBox("Register Student")
        layout = QGridLayout()

        self.student_combo = QComboBox()
        self.course_combo = QComboBox()

        layout.addWidget(QLabel("Student:"), 0, 0)
        layout.addWidget(self.student_combo, 0, 1)

        layout.addWidget(QLabel("Course:"), 1, 0)
        layout.addWidget(self.course_combo, 1, 1)

        button = QPushButton("Register Student")
        button.clicked.connect(self.register_student)

        layout.addWidget(button, 2, 0, 1, 2)

        group.setLayout(layout)
        self.main_layout.addWidget(group)

    def create_search_section(self):
        """Create the search controls for filtering displayed records.

        :return: None
        :rtype: None
        """
        layout = QHBoxLayout()

        self.search_input = QLineEdit()

        search_button = QPushButton("Search")
        search_button.clicked.connect(self.search_records)

        show_all_button = QPushButton("Show All")
        show_all_button.clicked.connect(self.refresh_table)

        layout.addWidget(QLabel("Search:"))
        layout.addWidget(self.search_input)
        layout.addWidget(search_button)
        layout.addWidget(show_all_button)

        self.main_layout.addLayout(layout)

    def create_table(self):
        """Create the table used to display students, instructors, and courses.

        :return: None
        :rtype: None
        """
        self.table = QTableWidget()
        self.table.setColumnCount(4)

        self.table.setHorizontalHeaderLabels(
            [
                "Type",
                "ID",
                "Name",
                "Details"
            ]
        )

        self.main_layout.addWidget(self.table)

    def create_action_buttons(self):
        """Create buttons for editing, deleting, saving, loading, and exporting.

        :return: None
        :rtype: None
        """
        layout = QHBoxLayout()

        edit_button = QPushButton("Edit")
        delete_button = QPushButton("Delete")
        save_button = QPushButton("Save")
        load_button = QPushButton("Load")
        export_button = QPushButton("Export CSV")

        edit_button.clicked.connect(self.edit_selected)
        delete_button.clicked.connect(self.delete_selected)
        save_button.clicked.connect(self.save_data)
        load_button.clicked.connect(self.load_data)
        export_button.clicked.connect(self.export_csv)

        layout.addWidget(edit_button)
        layout.addWidget(delete_button)
        layout.addWidget(save_button)
        layout.addWidget(load_button)
        layout.addWidget(export_button)

        self.main_layout.addLayout(layout)

    def update_dropdowns(self):
        """Refresh the student, course, and instructor combo boxes.

        :return: None
        :rtype: None
        """
        self.student_combo.clear()
        self.course_combo.clear()
        self.course_instructor.clear()

        for student in students:
            self.student_combo.addItem(student.name)

        for course in courses:
            self.course_combo.addItem(course.course_name)

        for instructor in instructors:
            self.course_instructor.addItem(instructor.name)

    def refresh_table(self):
        """Clear the table and display all current school records.

        :return: None
        :rtype: None
        """
        self.table.setRowCount(0)

        for student in students:
            course_names = ", ".join(
                course.course_name
                for course in student.registered_courses
            )

            self.add_table_row(
                "Student",
                student.student_id,
                student.name,
                f"Courses: {course_names}"
            )

        for instructor in instructors:
            course_names = ", ".join(
                course.course_name
                for course in instructor.assigned_courses
            )

            self.add_table_row(
                "Instructor",
                instructor.instructor_id,
                instructor.name,
                f"Courses: {course_names}"
            )

        for course in courses:
            instructor_name = ""

            if course.instructor is not None:
                instructor_name = course.instructor.name

            self.add_table_row(
                "Course",
                course.course_id,
                course.course_name,
                f"Instructor: {instructor_name}"
            )

    def add_table_row(self, record_type, record_id, name, details):
        """Add one record to the table.

        :param record_type: Type of record being displayed.
        :type record_type: str
        :param record_id: Identifier of the record.
        :type record_id: str
        :param name: Name associated with the record.
        :type name: str
        :param details: Additional information about the record.
        :type details: str
        :return: None
        :rtype: None
        """
        row = self.table.rowCount()
        self.table.insertRow(row)

        self.table.setItem(row, 0, QTableWidgetItem(record_type))
        self.table.setItem(row, 1, QTableWidgetItem(record_id))
        self.table.setItem(row, 2, QTableWidgetItem(name))
        self.table.setItem(row, 3, QTableWidgetItem(details))

    def add_student(self):
        """Read the student fields, validate them, and add a new student.

        A message box is displayed if the student is added successfully or if
        invalid input causes a ``ValueError``.

        :return: None
        :rtype: None
        """
        try:
            name = self.student_name.text()
            age = int(self.student_age.text())
            email = self.student_email.text()
            student_id = self.student_id.text()

            if name == "" or student_id == "":
                raise ValueError("Name and Student ID cannot be empty.")

            student = Student(name, age, email, student_id)
            students.append(student)

            self.update_dropdowns()
            self.refresh_table()

            QMessageBox.information(
                self,
                "Success",
                "Student added successfully!"
            )

        except ValueError as error:
            QMessageBox.critical(
                self,
                "Error",
                str(error)
            )

    def add_instructor(self):
        """Read the instructor fields, validate them, and add an instructor.

        :return: None
        :rtype: None
        """
        try:
            name = self.instructor_name.text()
            age = int(self.instructor_age.text())
            email = self.instructor_email.text()
            instructor_id = self.instructor_id.text()

            if name == "" or instructor_id == "":
                raise ValueError("Name and Instructor ID cannot be empty.")

            instructor = Instructor(name, age, email, instructor_id)
            instructors.append(instructor)

            self.update_dropdowns()
            self.refresh_table()

            QMessageBox.information(
                self,
                "Success",
                "Instructor added successfully!"
            )

        except ValueError as error:
            QMessageBox.critical(
                self,
                "Error",
                str(error)
            )

    def add_course(self):
        """Create a course and assign the selected instructor to it.

        :return: None
        :rtype: None
        """
        course_id = self.course_id.text()
        course_name = self.course_name.text()
        instructor_name = self.course_instructor.currentText()

        if course_id == "" or course_name == "":
            QMessageBox.critical(
                self,
                "Error",
                "Course ID and Course Name cannot be empty."
            )
            return

        if instructor_name == "":
            QMessageBox.critical(
                self,
                "Error",
                "Please select an instructor."
            )
            return

        selected_instructor = None

        for instructor in instructors:
            if instructor.name == instructor_name:
                selected_instructor = instructor
                break

        course = Course(course_id, course_name, selected_instructor)
        courses.append(course)
        selected_instructor.assign_course(course)

        self.update_dropdowns()
        self.refresh_table()

        QMessageBox.information(
            self,
            "Success",
            "Course added successfully!"
        )

    def register_student(self):
        """Register the selected student in the selected course.

        The method prevents duplicate registration in the same course.

        :return: None
        :rtype: None
        """
        student_name = self.student_combo.currentText()
        course_name = self.course_combo.currentText()

        selected_student = None
        selected_course = None

        for student in students:
            if student.name == student_name:
                selected_student = student
                break

        for course in courses:
            if course.course_name == course_name:
                selected_course = course
                break

        if selected_student is None or selected_course is None:
            QMessageBox.critical(
                self,
                "Error",
                "Please select a student and course."
            )
            return

        if selected_course in selected_student.registered_courses:
            QMessageBox.critical(
                self,
                "Error",
                "Student is already registered in this course."
            )
            return

        selected_student.register_course(selected_course)
        selected_course.add_student(selected_student)

        self.refresh_table()

        QMessageBox.information(
            self,
            "Success",
            "Student registered successfully!"
        )

    def search_records(self):
        """Search students, instructors, and courses using the entered text.

        Matching records are displayed in the table.

        :return: None
        :rtype: None
        """
        text = self.search_input.text().lower()
        self.table.setRowCount(0)

        for student in students:
            courses_text = " ".join(
                course.course_name.lower()
                for course in student.registered_courses
            )

            if (
                text in student.name.lower()
                or text in student.student_id.lower()
                or text in courses_text
            ):
                self.add_table_row(
                    "Student",
                    student.student_id,
                    student.name,
                    "Courses: " + ", ".join(
                        course.course_name
                        for course in student.registered_courses
                    )
                )

        for instructor in instructors:
            courses_text = " ".join(
                course.course_name.lower()
                for course in instructor.assigned_courses
            )

            if (
                text in instructor.name.lower()
                or text in instructor.instructor_id.lower()
                or text in courses_text
            ):
                self.add_table_row(
                    "Instructor",
                    instructor.instructor_id,
                    instructor.name,
                    "Courses: " + ", ".join(
                        course.course_name
                        for course in instructor.assigned_courses
                    )
                )

        for course in courses:
            instructor_name = ""

            if course.instructor is not None:
                instructor_name = course.instructor.name

            if (
                text in course.course_name.lower()
                or text in course.course_id.lower()
                or text in instructor_name.lower()
            ):
                self.add_table_row(
                    "Course",
                    course.course_id,
                    course.course_name,
                    f"Instructor: {instructor_name}"
                )

    def delete_selected(self):
        """Delete the record currently selected in the table.

        Related course registrations and instructor assignments are updated
        before the record is removed.

        :return: None
        :rtype: None
        """
        row = self.table.currentRow()

        if row == -1:
            QMessageBox.critical(
                self,
                "Error",
                "Please select a record."
            )
            return

        record_type = self.table.item(row, 0).text()
        record_id = self.table.item(row, 1).text()

        if record_type == "Student":
            for student in students:
                if student.student_id == record_id:
                    for course in courses:
                        if student in course.enrolled_students:
                            course.enrolled_students.remove(student)

                    students.remove(student)
                    break

        elif record_type == "Instructor":
            for instructor in instructors:
                if instructor.instructor_id == record_id:
                    for course in courses:
                        if course.instructor == instructor:
                            course.instructor = None

                    instructors.remove(instructor)
                    break

        elif record_type == "Course":
            for course in courses:
                if course.course_id == record_id:
                    for student in students:
                        if course in student.registered_courses:
                            student.registered_courses.remove(course)

                    for instructor in instructors:
                        if course in instructor.assigned_courses:
                            instructor.assigned_courses.remove(course)

                    courses.remove(course)
                    break

        self.update_dropdowns()
        self.refresh_table()

        QMessageBox.information(
            self,
            "Success",
            "Record deleted successfully!"
        )

    def edit_selected(self):
        """Edit the record currently selected in the table.

        Input dialogs are used to update student, instructor, or course data.

        :return: None
        :rtype: None
        """
        row = self.table.currentRow()

        if row == -1:
            QMessageBox.critical(
                self,
                "Error",
                "Please select a record."
            )
            return

        record_type = self.table.item(row, 0).text()
        record_id = self.table.item(row, 1).text()

        if record_type == "Student":
            for student in students:
                if student.student_id == record_id:
                    new_name, ok = QInputDialog.getText(
                        self,
                        "Edit Student",
                        "Name:",
                        text=student.name
                    )

                    if not ok:
                        return

                    new_age, ok = QInputDialog.getInt(
                        self,
                        "Edit Student",
                        "Age:",
                        student.age,
                        0
                    )

                    if not ok:
                        return

                    new_email, ok = QInputDialog.getText(
                        self,
                        "Edit Student",
                        "Email:",
                        text=student._email
                    )

                    if not ok:
                        return

                    new_id, ok = QInputDialog.getText(
                        self,
                        "Edit Student",
                        "Student ID:",
                        text=student.student_id
                    )

                    if not ok:
                        return

                    try:
                        Student(new_name, new_age, new_email, new_id)

                        student.name = new_name
                        student.age = new_age
                        student._email = new_email
                        student.student_id = new_id

                    except ValueError as error:
                        QMessageBox.critical(
                            self,
                            "Error",
                            str(error)
                        )
                        return

                    break

        elif record_type == "Instructor":
            for instructor in instructors:
                if instructor.instructor_id == record_id:
                    new_name, ok = QInputDialog.getText(
                        self,
                        "Edit Instructor",
                        "Name:",
                        text=instructor.name
                    )

                    if not ok:
                        return

                    new_age, ok = QInputDialog.getInt(
                        self,
                        "Edit Instructor",
                        "Age:",
                        instructor.age,
                        0
                    )

                    if not ok:
                        return

                    new_email, ok = QInputDialog.getText(
                        self,
                        "Edit Instructor",
                        "Email:",
                        text=instructor._email
                    )

                    if not ok:
                        return

                    new_id, ok = QInputDialog.getText(
                        self,
                        "Edit Instructor",
                        "Instructor ID:",
                        text=instructor.instructor_id
                    )

                    if not ok:
                        return

                    try:
                        Instructor(new_name, new_age, new_email, new_id)

                        instructor.name = new_name
                        instructor.age = new_age
                        instructor._email = new_email
                        instructor.instructor_id = new_id

                    except ValueError as error:
                        QMessageBox.critical(
                            self,
                            "Error",
                            str(error)
                        )
                        return

                    break

        elif record_type == "Course":
            for course in courses:
                if course.course_id == record_id:
                    new_id, ok = QInputDialog.getText(
                        self,
                        "Edit Course",
                        "Course ID:",
                        text=course.course_id
                    )

                    if not ok:
                        return

                    new_name, ok = QInputDialog.getText(
                        self,
                        "Edit Course",
                        "Course Name:",
                        text=course.course_name
                    )

                    if not ok:
                        return

                    instructor_names = [
                        instructor.name
                        for instructor in instructors
                    ]

                    if len(instructor_names) == 0:
                        QMessageBox.critical(
                            self,
                            "Error",
                            "No instructors available."
                        )
                        return

                    current_index = 0

                    if course.instructor is not None:
                        if course.instructor.name in instructor_names:
                            current_index = instructor_names.index(
                                course.instructor.name
                            )

                    new_instructor_name, ok = QInputDialog.getItem(
                        self,
                        "Edit Course",
                        "Instructor:",
                        instructor_names,
                        current_index,
                        False
                    )

                    if not ok:
                        return

                    new_instructor = None

                    for instructor in instructors:
                        if instructor.name == new_instructor_name:
                            new_instructor = instructor
                            break

                    old_instructor = course.instructor

                    if (
                        old_instructor is not None
                        and course in old_instructor.assigned_courses
                    ):
                        old_instructor.assigned_courses.remove(course)

                    course.course_id = new_id
                    course.course_name = new_name
                    course.instructor = new_instructor

                    if course not in new_instructor.assigned_courses:
                        new_instructor.assign_course(course)

                    break

        self.update_dropdowns()
        self.refresh_table()

        QMessageBox.information(
            self,
            "Success",
            "Record updated successfully!"
        )

    def save_data(self):
        """Save all current school records to a JSON file chosen by the user.

        :return: None
        :rtype: None
        """
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save Data",
            "",
            "JSON Files (*.json)"
        )

        if file_path == "":
            return

        if not file_path.endswith(".json"):
            file_path += ".json"

        data = {
            "students": [],
            "instructors": [],
            "courses": []
        }

        for student in students:
            data["students"].append(
                {
                    "name": student.name,
                    "age": student.age,
                    "email": student._email,
                    "student_id": student.student_id,
                    "registered_courses": [
                        course.course_id
                        for course in student.registered_courses
                    ]
                }
            )

        for instructor in instructors:
            data["instructors"].append(
                {
                    "name": instructor.name,
                    "age": instructor.age,
                    "email": instructor._email,
                    "instructor_id": instructor.instructor_id
                }
            )

        for course in courses:
            instructor_id = None

            if course.instructor is not None:
                instructor_id = course.instructor.instructor_id

            data["courses"].append(
                {
                    "course_id": course.course_id,
                    "course_name": course.course_name,
                    "instructor_id": instructor_id
                }
            )

        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)

        QMessageBox.information(
            self,
            "Success",
            "Data saved successfully!"
        )

    def load_data(self):
        """Load school records from a JSON file chosen by the user.

        Existing lists are cleared and recreated from the saved data.

        :return: None
        :rtype: None
        """
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Load Data",
            "",
            "JSON Files (*.json)"
        )

        if file_path == "":
            return

        try:
            with open(file_path, "r") as file:
                data = json.load(file)

            students.clear()
            instructors.clear()
            courses.clear()

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
                            course.add_student(selected_student)
                            break

            self.update_dropdowns()
            self.refresh_table()

            QMessageBox.information(
                self,
                "Success",
                "Data loaded successfully!"
            )

        except Exception as error:
            QMessageBox.critical(
                self,
                "Error",
                str(error)
            )

    def export_csv(self):
        """Export all current school records to a CSV file.

        :return: None
        :rtype: None
        """
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Export CSV",
            "",
            "CSV Files (*.csv)"
        )

        if file_path == "":
            return

        if not file_path.endswith(".csv"):
            file_path += ".csv"

        with open(file_path, "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow(
                [
                    "Type",
                    "ID",
                    "Name",
                    "Details"
                ]
            )

            for student in students:
                course_names = ", ".join(
                    course.course_name
                    for course in student.registered_courses
                )

                writer.writerow(
                    [
                        "Student",
                        student.student_id,
                        student.name,
                        f"Courses: {course_names}"
                    ]
                )

            for instructor in instructors:
                course_names = ", ".join(
                    course.course_name
                    for course in instructor.assigned_courses
                )

                writer.writerow(
                    [
                        "Instructor",
                        instructor.instructor_id,
                        instructor.name,
                        f"Courses: {course_names}"
                    ]
                )

            for course in courses:
                instructor_name = ""

                if course.instructor is not None:
                    instructor_name = course.instructor.name

                writer.writerow(
                    [
                        "Course",
                        course.course_id,
                        course.course_name,
                        f"Instructor: {instructor_name}"
                    ]
                )

        QMessageBox.information(
            self,
            "Success",
            "CSV exported successfully!"
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = SchoolManagementSystem()
    window.show()

    sys.exit(app.exec_())
