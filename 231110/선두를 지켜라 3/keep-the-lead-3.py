MAX_POS = 1000001

n, m = map(int, input().split())
posA, posB = [0] * MAX_POS, [0] * MAX_POS

# A 이동 기록
timeA = 1
for _ in range(n):
    v, t = map(int, input().split())
    for _ in range(t):
        posA[timeA] = posA[timeA-1] + v
        timeA += 1

# B 이동 기록
timeB = 1
for _ in range(m):
    v, t = map(int, input().split())
    for _ in range(t):
        posB[timeB] = posB[timeB-1] + v
        timeB += 1

# 명예의 전당 조합 기록 (leader=1:A 2:B 3:A,B)
leader, res = 0, 0
for i in range(1, timeA+1):
    if posA[i] > posB[i]:
        if leader != 1:
            res += 1
        leader = 1
    elif posA[i] < posB[i]:
        if leader != 2:
            res += 1
        leader = 2
    else:
        if leader != 3:
            res += 1
        leader = 3

print(res-1)