marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 95
}

sorted_dict = dict(sorted(marks.items(), key=lambda x: x[1]))

print(sorted_dict)