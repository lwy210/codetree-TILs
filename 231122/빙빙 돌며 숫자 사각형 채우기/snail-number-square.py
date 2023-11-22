n, m = map(int, input().split())

# 오른쪽, 아래쪽, 왼쪽, 위쪽 순서
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

x, y = 0, 0
dir_num = 0

answer = [[0] * n for _ in range(m)]
answer[0][0] = 1

def in_range(x, y):
    return 0 <= x < m and 0 <= y < n

for i in range(2, n*m + 1):
    nx, ny = x + dxs[dir_num], y + dys[dir_num]
    if not in_range(nx, ny) or answer[nx][ny] != 0:
        dir_num = (dir_num + 1) % 4
    
    x, y = x + dxs[dir_num], y + dys[dir_num]
    answer[x][y] = i

for i in range(n):
    for j in range(m):
        print(answer[i][j], end=' ')
    print()