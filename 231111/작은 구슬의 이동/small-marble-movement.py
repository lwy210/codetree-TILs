n, t = map(int, input().split())
r, c, d = map(str, input().split())

mapper = {'R':0, 'D':1, 'U':2, 'L':3}

x, y = int(r)-1, int(c)-1 # r행 c열 구슬의 초기 위치
n_dir = mapper[d] # 초기 방향

dxs = [0, 1, -1, 0]
dys = [1, 0, 0, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

for _ in range(t):
    nx, ny = x + dxs[n_dir], y + dys[n_dir]
    if not in_range(nx, ny):
        n_dir = 3 - n_dir
    else:
        x, y = nx, ny

print(x+1, y+1)