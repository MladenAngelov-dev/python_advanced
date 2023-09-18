n = int(input())

unique = set()

for _ in range(n):
    element = input().split()
    for el in element:
        unique.add(el)

for uniq in unique:
    print(uniq)