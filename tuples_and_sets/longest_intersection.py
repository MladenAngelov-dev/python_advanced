# n = 3
#
# one = [3,5]
# two = [1,2]
#
# for numb in range(one[0], one[1]+1):
#     print(numb)

n = int(input())

longest_intersection = set()

for _ in range(n):
    one, two = [element.split(",") for element in input().split("-")]

    range_one = set(range(int(one[0]), int(one[1])+1))
    range_two = set(range(int(two[0]), int(two[1])+1))

    intersection = range_one & range_two

    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

print(f"Longest intersection is "
      f"[{', '.join(str(x) for x in longest_intersection)}]"
      f" with length {len(longest_intersection)}")
