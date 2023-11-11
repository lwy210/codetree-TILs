directions = {'W':[-1, 0], 'S':[0, -1], 'N':[0, 1], 'E':[1, 0]}

x, y = 0, 0
n = int(input())

for _ in range(n):
    d, num = map(str, input().split())
    x, y = x + directions[d][0] * int(num), y + directions[d][1] * int(num)

print(x, y)