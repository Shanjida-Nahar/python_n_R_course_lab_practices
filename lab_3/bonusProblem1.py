numbers = list(map(int, input("Enter numbers: ").split()))

largest = second = numbers[0]

for num in numbers:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print("Second largest =", second)