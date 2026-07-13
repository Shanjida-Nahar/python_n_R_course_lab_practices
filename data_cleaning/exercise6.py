import pandas as pd

students = pd.read_csv("students_dirty_dataset.csv")

invalid_age = students[
    (students["Age"] < 16) |
    (students["Age"] > 100)
]

print(invalid_age)