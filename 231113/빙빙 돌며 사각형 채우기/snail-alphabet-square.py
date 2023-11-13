n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

# 우, 하, 좌, 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 초기값
arr[0][0] = 'A'
x, y, n_dir = 0, 0, 0

for i in range(1, n*m):
    nx, ny = x + dx[n_dir], y + dy[n_dir]
    if not in_range(nx, ny) or arr[nx][ny] != 0:
        n_dir = (n_dir + 1) % 4
    
    x, y = x + dx[n_dir], y + dy[n_dir]
    arr[x][y] = chr((ord('A')+(i%26)))

for i in range(n):
    for j in range(m):
        print(arr[i][j], end = ' ')
    print()