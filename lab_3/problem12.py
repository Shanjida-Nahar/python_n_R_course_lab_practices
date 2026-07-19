students = ["Alice", "Bob", "Charlie"]

students.append(input("Enter new student: "))
students.insert(1, input("Enter student to insert at position 2: "))

remove_name = input("Enter student name to remove: ")
if remove_name in students:
    students.remove(remove_name)

students.sort()

print(students)