numbers = list(map(int, input("Enter numbers: ").split()))

total = 0
maximum = numbers[0]
minimum = numbers[0]

for num in numbers:
    total += num
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num

average = total / len(numbers)

print("Sum =", total)
print("Average =", average)
print("Maximum =", maximum)
print("Minimum =", minimum)