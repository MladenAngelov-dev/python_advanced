# n = int(input())
#
# unique_names = set()
#
# for _ in range(n):
#     name = input()
#     unique_names.add(name)
#
# for unique in unique_names:
#     print(unique)

def get_unique_name(n):
    unique_names = set()

    for _ in range(n):
        name = input()
        unique_names.add(name)

    return unique_names


def print_unique_names(unique_names):
    for unique in unique_names:
        print(unique)


n = int(input())
unique_names = get_unique_name(n)
print_unique_names(unique_names)