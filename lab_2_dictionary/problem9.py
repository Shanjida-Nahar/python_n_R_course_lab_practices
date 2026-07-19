student = {
    "Name": "Rahim",
    "ID": "221001",
    "Department": "CSE"
}

key = input("Enter key: ")

if key in student:
    print("Key exists.")
else:
    print("Key does not exist.")