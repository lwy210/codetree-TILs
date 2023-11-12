dxs = [-1, 0, 0, 1]
dys = [0, -1, 1, 0]
mapper = {'W':0, 'S':1, 'N':2, 'E':3}

n = int(input())
x, y = 0, 0
res = 0
arrived = False

for _ in range(n):
    direction, distance = map(str, input().split())
    n_dir = mapper[direction]

    for _ in range(int(distance)):
        x, y = x + dxs[n_dir], y + dys[n_dir]
        res += 1
        if x == 0 and y == 0 and not arrived:
            arrived = True
            break
    if arrived:
        break

if arrived:
    print(res)
else:
    print(-1)