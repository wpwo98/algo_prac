N = int(input())
cnt = 0
for i in range(0, N//5 + 1):
    for j in range(0, N//3 + 1):
        if 5*i + 3*j == N:
            cnt = i+j

if cnt == 0:
    print(-1)
else:
    print(cnt)
