measures = [23, 345, 45, 56, 3, 4, 45, 34, 4, 356,
            45, 34, 4, 45, 34, 345, 6, 34, 4, 345, 43]

count = 0
for m in measures:
    count += 1

print(count)

print()
count = sum(1 for _ in measures)

print(count)
