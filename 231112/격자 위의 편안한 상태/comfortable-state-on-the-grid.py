n, m = map(int, input().split())

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

arr = [[0] * n for _ in range(n)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

for _ in range(m):
    r, c = map(int, input().split()) # 행, 열
    x, y = c-1, r-1

    arr[y][x] = 1

    cnt = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if in_range(nx, ny) and arr[ny][nx] == 1:
            cnt += 1

    if cnt == 3:
        print(1)
    else:
        print(0)