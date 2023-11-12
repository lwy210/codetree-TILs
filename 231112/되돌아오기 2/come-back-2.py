# 북, 동, 남, 서
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

# 초기값
x, y = 0, 0
n_dir = 0
arrived = False
res = 0

# 입력
command = list(input())

# 로직
for c in command:
    # 명령 처리
    if c == 'L':
        n_dir = (n_dir + 3) % 4
    elif c == 'R':
        n_dir = (n_dir - 1) % 4
    else: # c == 'F'
        x, y = x + dxs[n_dir], y + dys[n_dir]
    
    res += 1 # 1초 소요

    # 0,0에 도착했는지 확인
    if x == 0 and y == 0 and not arrived:
        arrived = True
        break

# 출력
if arrived:
    print(res)
else:
    print(-1)