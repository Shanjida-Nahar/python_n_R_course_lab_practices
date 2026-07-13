numbers = list(map(int, input().split()))

total = sum(numbers)
average = total / len(numbers)
largest = max(numbers)
smallest = min(numbers)

print("Sum =", total)
print("Average =", average)
print("Largest =", largest)
print("Smallest =", smallest)