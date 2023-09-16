numbers = input().split()

for num in range(len(numbers)):
    print(numbers.pop(), end=" ")