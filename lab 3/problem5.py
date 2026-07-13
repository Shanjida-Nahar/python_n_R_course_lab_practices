numbers = list(map(int, input("Enter numbers: ").split()))

even_list = []

for num in numbers:
    if num % 2 == 0:
        even_list.append(num)

print(even_list)