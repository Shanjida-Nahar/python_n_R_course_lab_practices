import pandas as pd

students = pd.read_csv("students_dirty_dataset.csv")

duplicate_students = students[
    students.duplicated(subset="StudentID", keep=False)
]

print(duplicate_students)