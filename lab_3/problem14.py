numbers = list(map(int, input("Enter numbers: ").split()))

print("First three:", numbers[:3])
print("Last three:", numbers[-3:])
print("Every second:", numbers[::2])
print("Reverse:", numbers[::-1])