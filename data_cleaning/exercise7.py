import pandas as pd

students = pd.read_csv("students_dirty_dataset.csv")

invalid_attendance = students[
    (students["Attendance"] < 0) |
    (students["Attendance"] > 100)
]

print(invalid_attendance)