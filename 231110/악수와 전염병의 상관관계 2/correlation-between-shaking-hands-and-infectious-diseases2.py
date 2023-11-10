# n:개발자의 수, k:전염병옮는악수횟수, p:전염병걸린개발자, tt:악수횟수
n, k, p, tt = map(int, input().split())
state = [0] * (n+1) # 0:음성 1:양성
state[p] = 1
arr = []
klist = [k] * (n+1) 

for _ in range(tt):
    # t초에 x개발자와 y개발자가 악수를 나눴다.
    t, x, y = map(int, input().split())
    arr.append([t, x, y])

# 시간순으로 정렬
arr = sorted(arr, key = lambda x : x[0])

# 감염 여부 체크
for a in arr:
    t, x, y = map(int, a)
    if state[x] == 1 and klist[x] > 0 and state[y] == 1 and klist[y] > 0:
        klist[x] -= 1
        klist[y] -= 1
    elif state[x] == 1 and klist[x] > 0:
        state[y] = 1
        klist[x] -= 1
    elif state[y] == 1 and klist[y] > 0:
        state[x] = 1
        klist[y] -= 1

print(''.join(map(str, state[1:])))