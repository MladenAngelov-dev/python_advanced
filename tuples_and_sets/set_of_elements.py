# x, y = map(int, input().split())
#
# x_set = set()
# y_set = set()
#
# for _ in range(x):
#     x_numbers = input()
#     x_set.add(x_numbers)
# for _ in range(y):
#     y_numbers = input()
#     y_set.add(y_numbers)
#
# common_element = x_set & y_set
# for common in common_element:
#     print(common)

x, y = map(int, input().split())

x_set = {input() for _ in range(x)}
y_set = {input() for _ in range(y)}

common_elements = x_set & y_set
for common in common_elements:
    print(common)
