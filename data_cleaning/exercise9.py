import pandas as pd

students = pd.read_csv("students_dirty_dataset.csv")

valid_age = students["Age"].between(16, 100)

median_age = students.loc[
    valid_age,
    "Age"
].median()

students.loc[
    ~valid_age | students["Age"].isnull(),
    "Age"
] = median_age

print(students)