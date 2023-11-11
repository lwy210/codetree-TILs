def in_range(n, x, y):
    return 0 < x <= n and 0 < y <= n

dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]
mapper = {'U':0, 'D':3, 'R':1, 'L':2}

n, t = map(int, input().split())
r, c, d = map(str, input().split())
x, y = int(c), int(r) # r행 c열
n_dir = mapper[d]

for _ in range(t):
    nx, ny = x + dxs[n_dir], y + dys[n_dir] # 1
    if not in_range(n, nx, ny):
        n_dir = 3 - n_dir
    else:
        x, y = nx, ny

print(y, x)