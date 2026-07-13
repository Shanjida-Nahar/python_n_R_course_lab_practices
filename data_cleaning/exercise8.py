import pandas as pd

students = pd.read_csv("students_dirty_dataset.csv")

students["Physics"] = pd.to_numeric(
    students["Physics"],
    errors="coerce"
)

print(students["Physics"])