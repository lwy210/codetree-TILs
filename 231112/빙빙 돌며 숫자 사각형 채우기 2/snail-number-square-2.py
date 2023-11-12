n, m = map(int, input().split())

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

# 남, 동, 북, 서
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
arr = [[0] * n for _ in range(m)]

# 초기값
n_dir = 0
arr[0][0] = 1
x, y = 0, 0

# 로직
for i in range(2, n*m + 1):
    nx, ny = x + dx[n_dir], y + dy[n_dir]
    if not in_range(nx, ny) or arr[nx][ny] != 0:
        n_dir = (n_dir + 1) % 4
    x, y = x + dx[n_dir], y + dy[n_dir] # 여기를 x, y = nx, ny로 하면 안됨
    arr[x][y] = i

# 출력
for i in range(m):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()