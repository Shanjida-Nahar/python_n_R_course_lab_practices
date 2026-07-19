numbers = list(map(int, input("Enter numbers: ").split()))

search = int(input("Enter number to search: "))

if search in numbers:
    print("Found at index", numbers.index(search))
else:
    print("Not found")