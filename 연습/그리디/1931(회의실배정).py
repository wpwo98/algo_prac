N = int(input())
s = []

for i in range(N):
    first, second = map(int,input().split())
    s.append([first, second])

s = sorted(s, key=lambda a: a[0])
s = sorted(s, key=lambda a: a[1])

last, cnt = 0, 0

for i, j in s:
    if i >= last:
        cnt += 1
        last = j

print(cnt)