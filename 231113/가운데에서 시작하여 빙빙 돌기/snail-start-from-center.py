n = int(input())
arr = [[0] * n for _ in range(n)]

# 우, 상, 좌, 하
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

# 초기값
x, y, n_dir, n_num = n//2, n//2, 0, 1

# 범위에서 벗어나면 (종료 조건)
def end():
    return not (0 <= x < n and 0 <= y < n)

# 로직
cnt = 1
while not end():
    for _ in range(n_num):                  # 현재 방향에서 n_num 만큼 이동
        arr[x][y] = cnt                     # 기록
        cnt += 1                            # 기록할 숫자
        x, y = x + dx[n_dir], y + dy[n_dir] # 이동

        if end():                           # 범위에서 벗어나면 종료
            break

    n_dir = (n_dir + 1) % 4                 # 방향 바꾸기
    if n_dir == 0 or n_dir == 2:            # 좌, 우 방향일 때는 이동 횟수 +1
        n_num += 1

# 출력
for i in range(n):
    for j in range(n):
        print(arr[i][j], end = ' ')
    print()