n, m = map(int, input().split())

def in_range(x, y):
    return 0 <= x < m and 0 <= y < n

# 남, 동, 북, 서
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
arr = [[0] * m for _ in range(n)]

# 초기값
n_dir = 0
arr[0][0] = 1
x, y = 0, 0

# 로직
for i in range(2, n*m + 1):
    nx, ny = x + dx[n_dir], y + dy[n_dir]
    if not in_range(nx, ny) or arr[ny][nx] != 0:
        n_dir = (n_dir + 1) % 4
    x, y = x + dx[n_dir], y + dy[n_dir] # 여기를 x, y = nx, ny로 하면 안됨
    arr[y][x] = i

# 출력
for i in range(m):
    for j in range(n):
        print(arr[j][i], end=' ')
    print()