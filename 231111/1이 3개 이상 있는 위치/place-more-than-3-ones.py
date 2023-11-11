def in_range(n, x, y):
    return 0 <= x < n and 0 <= y < n

dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
res = 0

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        cnt = 0
        for dx, dy in zip(dxs, dys):
            nx, ny = i+dx, j+dy
            if in_range(n, nx, ny) and arr[ny][nx] == 1:
                cnt += 1
        if cnt >= 3:
            res += 1

print(res)