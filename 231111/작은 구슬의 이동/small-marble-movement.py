def in_range(n, x, y):
    return 0 < x <= n and 0 < y <= n

dxs, dys = [0, -1, 1, 0], [1, 0, 0, -1]
mapper = {'U':0, 'L':1, 'R':2, 'D':3}

n, t = map(int, input().split())
r, c, d = map(str, input().split())
x, y = int(c), int(r) # r행 c열 구슬의 초기 위치
n_dir = mapper[d] # 초기 방향

for _ in range(t):
    nx, ny = x + dxs[n_dir], y + dys[n_dir] # 1
    if not in_range(n, nx, ny):
        n_dir = 3 - n_dir
        if t > 0: # 벽에 부딪히면 1초 소모
            t -= 1
    else:
        x, y = nx, ny

print(y, x)