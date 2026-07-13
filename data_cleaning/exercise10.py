import pandas as pd

students = pd.read_csv("students_dirty_dataset.csv")

students["Gender"] = (
    students["Gender"]
    .astype("string")
    .str.strip()
    .str.upper()
)

gender_map = {
    "M": "M",
    "MALE": "M",
    "F": "F",
    "FEMALE": "F"
}

students["Gender"] = (
    students["Gender"]
    .map(gender_map)
    .fillna("Unknown")
)

print(students)