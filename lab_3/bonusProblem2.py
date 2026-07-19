numbers = list(map(int, input("Enter numbers: ").split()))

last = numbers[-1]
numbers.pop()
numbers.insert(0, last)

print(numbers)