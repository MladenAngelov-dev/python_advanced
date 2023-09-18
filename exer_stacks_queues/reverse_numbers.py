numb = [x for x in input().split()]
stack = []

while numb:
    stack.append(numb.pop())

print(" ".join(stack))