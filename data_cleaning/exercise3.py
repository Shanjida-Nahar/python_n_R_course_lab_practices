import pandas as pd

students = pd.read_csv("students_dirty_dataset.csv")

missing_rows = students[students.isnull().any(axis=1)]

print(missing_rows)