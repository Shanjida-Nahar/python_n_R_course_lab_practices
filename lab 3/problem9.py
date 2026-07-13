A = [1, 2, 3]
B = [4, 5, 6]

x = A.copy()
x.append(B)
print("append():", x)

y = A.copy()
y.extend(B)
print("extend():", y)

z = A + B
print("+ operator:", z)