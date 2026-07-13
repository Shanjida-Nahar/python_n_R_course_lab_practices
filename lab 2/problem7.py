numbers = list(map(int, input("Enter numbers: ").split()))

for i in numbers:
    if numbers.count(i) > 0:
        print(i, "->", numbers.count(i))
        while i in numbers:
            numbers.remove(i)