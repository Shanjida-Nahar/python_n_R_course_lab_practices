numbers = list(map(int, input("Enter numbers: ").split()))

a = numbers.copy()
a.reverse()
print("Using reverse():", a)

print("Using slicing:", numbers[::-1])