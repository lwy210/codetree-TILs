# 입력
n, t = map(int, input().split())
command = list(input())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

# 범위
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 초기 값 설정
x, y, n_dir = n//2, n//2, 0
res = arr[x][y]

# 로직
for c in command:
    if c == 'L':
        n_dir = (n_dir + 3) % 4
    elif c == 'R':
        n_dir = (n_dir + 1) % 4
    else:
        nx, ny = x + dx[n_dir], y + dy[n_dir]
        if in_range(nx, ny):
            res += arr[nx][ny]
            x, y = x + dx[n_dir], y + dy[n_dir]

# 출력
print(res)