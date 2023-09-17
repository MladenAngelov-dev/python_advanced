from collections import deque

stock = int(input())

orders = deque(int(x) for x in input().split())
print(max(orders))

while orders:
    current_order = orders[0]
    if current_order <= stock:
        stock -= current_order
        orders.popleft()
    else:
        break

if orders:
    print(f"Orders left:", end="")
    while orders:
        print(f" {orders.popleft()}", end="")
else:
    print("Orders complete")
