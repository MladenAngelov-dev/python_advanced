from collections import deque

chocolates = deque(int(x) for x in input().split(", "))
cups_of_milk = deque(int(x) for x in input().split(", "))

milkshakes = 0

while milkshakes != 5 and chocolates and cups_of_milk:
    choco = chocolates.pop()
    milk = cups_of_milk.popleft()

    if choco <= 0 and milk <= 0:
        continue
    elif choco <= 0:
        cups_of_milk.appendleft(milk)
        continue
    elif milk <= 0:
        chocolates.append(choco)
        continue

    if choco == milk:
        milkshakes += 1
    else:
        cups_of_milk.append(milk)
        chocolates.append(choco - 5)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print(f"Chocolate: {', '.join(str(x) for x in chocolates) or 'empty'}")
print(f"Milk: {', '.join(str(x) for x in cups_of_milk) or 'empty'}")