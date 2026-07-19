names = []

for i in range(5):
    name = input("Enter name: ")
    names.append(name)

names.sort()

print("Sorted names:")
for name in names:
    print(name)