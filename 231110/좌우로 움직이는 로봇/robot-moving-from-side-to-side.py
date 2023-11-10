MAX_POS = 1000001
posA, posB = [0] * MAX_POS, [0] * MAX_POS

n, m = map(int, input().split())

# 로봇 A 이동 기록
timeA = 1
for _ in range(n):
    t, d = map(str, input().split())
    if d == 'L':
        for _ in range(int(t)):
            posA[timeA] = posA[timeA-1] - 1
            timeA += 1
    elif d == 'R':
        for _ in range(int(t)):
            posA[timeA] = posA[timeA-1] + 1
            timeA += 1
posA[timeA:] = [posA[timeA-1]] * len(posA[timeA:]) # 움직임 종료 이후 같은 위치 유지

# 로봇 B 이동 기록
timeB = 1
for _ in range(m):
    t, d = map(str, input().split())
    if d == 'L':
        for _ in range(int(t)):
            posB[timeB] = posB[timeB-1] - 1
            timeB += 1
    elif d == 'R':
        for _ in range(int(t)):
            posB[timeB] = posB[timeB-1] + 1
            timeB += 1
posB[timeB:] = [posB[timeB-1]] * len(posB[timeB:]) # 움직임 종료 이후 같은 위치 유지

# 바로 직전에 다른 위치에 있다가 그 다음 번에 같은 위치에 오게 되는 경우 count
state, res = 0, 0 # state 1=다른위치, 2=같은 위치
for i in range(1, max(timeA, timeB)):
    if posA[i] == posB[i]:
        if state == 1:
            res += 1
        state = 2
    else:
        state = 1

print(res)