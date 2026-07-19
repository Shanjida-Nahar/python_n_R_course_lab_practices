import pandas as pd
filepath=
def read_excel_file(file_path):
    try:
        df = pd.read_excel(file_path)
        return df
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return None
    data=read_excel_file("students_dirty_dataset.xlsx")
    print(data)