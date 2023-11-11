# 북, 동, 남, 서 (0, 1, 2, 3)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
c_dir = 0

x, y = 0, 0
command = list(input())

for c in command:
    if c == 'L':
        c_dir = (c_dir + 3) % 4
    elif c == 'R':
        c_dir = (c_dir + 1) % 4
    else:
        x, y = x + dx[c_dir], y + dy[c_dir]

print(x, y)