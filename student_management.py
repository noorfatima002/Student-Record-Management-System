import json
import os


FILE_NAME = "students.json"


# -----------------------------------------
# Load students from JSON file
# -----------------------------------------
def load_students():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except (json.JSONDecodeError, OSError):
        return []


# -----------------------------------------
# Save students to JSON file
# -----------------------------------------
def save_students(students):
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(students, file, indent=4)

    except OSError:
        print("Error: Could not save student data.")


# -----------------------------------------
# Find student by ID
# -----------------------------------------
def find_student(students, student_id):
    for student in students:
        if student["id"].lower() == student_id.lower():
            return student

    return None


# -----------------------------------------
# Add Student
# -----------------------------------------
def add_student(students):

    print("\n===== Add Student =====")

    student_id = input("Enter Student ID: ").strip()

    if not student_id:
        print("Student ID cannot be empty.")
        return

    if find_student(students, student_id):
        print("A student with this ID already exists.")
        return

    name = input("Enter Student Name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    # Age validation
    while True:
        try:
            age = int(input("Enter Age: "))

            if age <= 0:
                print("Age must be greater than 0.")
            else:
                break

        except ValueError:
            print("Please enter a valid number for age.")

    course = input("Enter Course: ").strip()

    if not course:
        print("Course cannot be empty.")
        return

    # Marks validation
    while True:
        try:
            marks = float(input("Enter Marks (0-100): "))

            if 0 <= marks <= 100:
                break
            else:
                print("Marks must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number for marks.")

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course,
        "marks": marks
    }

    students.append(student)
    save_students(students)

    print("Student added successfully!")


# -----------------------------------------
# View Students
# -----------------------------------------
def view_students(students):

    print("\n===== Student Records =====")

    if not students:
        print("No student records found.")
        return

    for student in students:
        print("------------------------------")
        print(f"ID     : {student['id']}")
        print(f"Name   : {student['name']}")
        print(f"Age    : {student['age']}")
        print(f"Course : {student['course']}")
        print(f"Marks  : {student['marks']}")

    print("------------------------------")


# -----------------------------------------
# Search Student
# -----------------------------------------
def search_student(students):

    print("\n===== Search Student =====")

    student_id = input("Enter Student ID: ").strip()

    student = find_student(students, student_id)

    if student:
        print("\nStudent Found!")
        print(f"ID     : {student['id']}")
        print(f"Name   : {student['name']}")
        print(f"Age    : {student['age']}")
        print(f"Course : {student['course']}")
        print(f"Marks  : {student['marks']}")

    else:
        print("Student not found.")


# -----------------------------------------
# Update Student
# -----------------------------------------
def update_student(students):

    print("\n===== Update Student =====")

    student_id = input("Enter Student ID: ").strip()

    student = find_student(students, student_id)

    if not student:
        print("Student not found.")
        return

    print("Press Enter to keep the existing value.")

    name = input(f"Enter Name [{student['name']}]: ").strip()

    if name:
        student["name"] = name

    age_input = input(f"Enter Age [{student['age']}]: ").strip()

    if age_input:
        try:
            age = int(age_input)

            if age > 0:
                student["age"] = age
            else:
                print("Invalid age. Old age kept.")

        except ValueError:
            print("Invalid age. Old age kept.")

    course = input(f"Enter Course [{student['course']}]: ").strip()

    if course:
        student["course"] = course

    marks_input = input(f"Enter Marks [{student['marks']}]: ").strip()

    if marks_input:
        try:
            marks = float(marks_input)

            if 0 <= marks <= 100:
                student["marks"] = marks
            else:
                print("Invalid marks. Old marks kept.")

        except ValueError:
            print("Invalid marks. Old marks kept.")

    save_students(students)

    print("Student updated successfully!")


# -----------------------------------------
# Delete Student
# -----------------------------------------
def delete_student(students):

    print("\n===== Delete Student =====")

    student_id = input("Enter Student ID: ").strip()

    student = find_student(students, student_id)

    if not student:
        print("Student not found.")
        return

    print(f"Student: {student['name']}")

    confirmation = input("Are you sure you want to delete? (y/n): ")

    if confirmation.lower() == "y":
        students.remove(student)
        save_students(students)
        print("Student deleted successfully!")

    else:
        print("Delete operation cancelled.")


# -----------------------------------------
# Show Summary
# -----------------------------------------
def show_summary(students):

    print("\n===== Marks Summary =====")

    if not students:
        print("No student records available.")
        return

    marks = [student["marks"] for student in students]

    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    highest_student = next(
        student for student in students
        if student["marks"] == highest
    )

    lowest_student = next(
        student for student in students
        if student["marks"] == lowest
    )

    print(f"Average Marks : {average:.2f}")
    print(
        f"Highest Marks : {highest} "
        f"({highest_student['name']})"
    )
    print(
        f"Lowest Marks  : {lowest} "
        f"({lowest_student['name']})"
    )


# -----------------------------------------
# Main Menu
# -----------------------------------------
def main():

    students = load_students()

    while True:

        print("\n======================================")
        print("   STUDENT RECORD MANAGEMENT SYSTEM")
        print("======================================")

        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Show Summary")
        print("7. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_student(students)

        elif choice == "2":
            view_students(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            update_student(students)

        elif choice == "5":
            delete_student(students)

        elif choice == "6":
            show_summary(students)

        elif choice == "7":
            print("Thank you for using the system!")
            break

        else:
            print("Invalid choice. Please select 1-7.")


# -----------------------------------------
# Program starts here
# -----------------------------------------
if __name__ == "__main__":
    main()