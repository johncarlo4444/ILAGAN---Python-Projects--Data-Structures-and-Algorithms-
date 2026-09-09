print("\nILAGAN PYTHON PROJECT - STUDENT LIST MENU\n")

print("""
=== STUDENT LIST MENU ===
1. Display all students
2. Display first and last student
3. Add a new student
4. Change a student's name
5. Remove a student
6. Display number of students
""")

students = ["Carlo", "Zanch", "Axcel", "Raniel", "Renji", "Glen"]

choice = input("Enter your choice (1-6): ")


if choice == "1":
    print(students)

elif choice == "2":
    print("First student: ", students[0])
    print("Last student: ", students[-1])

elif choice == "3":
    newstudent = input("Add a new student: ")
    students.append(newstudent)
    print("Student added:", students)

elif choice == "4":
    print(f"Student's List: {students}")
    student_to_change = input("Enter student name to change: ")
    newname = input("Enter new name: ")

    if student_to_change in students:
        idx = students.index(student_to_change)
        print(idx)
        students[idx] = newname
        print("Student changed:", students)
    else:
        print("Student not found")

elif choice == "5":
    print(f"Student's List: {students}")
    student_to_remove = input("Remove a student: ")

    if student_to_remove in students:
        students.remove(student_to_remove)
        print("Student removed:", students)
    else:
        print("Student not found")

elif choice == "6":
    print(len(students), "students are currently in the list")

else:
    print("Invalid choice. Enter your choice (1-6)")