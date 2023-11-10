MAX_POS = 1000001

posA = [0] * MAX_POS
posB = [0] * MAX_POS

n, m = map(int, input().split())

# A 이동 기록
timeA = 1
for _ in range(n):
    v, t = map(int, input().split())
    for i in range(t):
        posA[timeA] = posA[timeA-1] + v
        timeA += 1

# B 이동 기록
timeB = 1
for _ in range(m):
    v, t = map(int, input().split())
    for i in range(t):
        posB[timeB] = posB[timeB-1] + v
        timeB += 1

# 선두 기록 (A=1, B=2)
leader, res = 0, 0
for i in range(timeA):
    if posA[i] > posB[i]:
        if leader == 2:
            res += 1
        leader = 1
    elif posA[i] < posB[i]:
        if leader == 1:
            res += 1
        leader = 2

print(res)