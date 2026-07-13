import pandas as pd

students = pd.read_csv("students_dirty_dataset.csv")
sales = pd.read_csv("sales_dirty_dataset.csv")

print("Student shape:", students.shape)
print("Sales shape:", sales.shape)