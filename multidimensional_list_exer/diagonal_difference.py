n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]
primary = [matrix[i][i] for i in range(n)]
secondary = [matrix[i][-i - 1] for i in range(n)]

print(abs(sum(primary) - sum(secondary)))