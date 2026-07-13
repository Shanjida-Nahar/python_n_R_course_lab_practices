numbers = list(map(int, input("Enter numbers: ").split()))

num = int(input("Enter number to count: "))

count = numbers.count(num)

print("Frequency =", count)