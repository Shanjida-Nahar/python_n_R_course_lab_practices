runs = []

for i in range(15):
    runs.append(int(input("Enter runs: ")))

total = sum(runs)
average = total / len(runs)
highest = max(runs)
lowest = min(runs)

half_century = 0
century = 0

for score in runs:
    if score >= 50:
        half_century += 1
    if score >= 100:
        century += 1

print("Total runs =", total)
print("Average =", average)
print("Highest =", highest)
print("Lowest =", lowest)
print("Half-centuries =", half_century)
print("Centuries =", century)