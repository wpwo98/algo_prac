N = int(input())
P = list(map(int, input().split()))
P.sort()
answer = 0
for i in range(len(P)):
    if i != 0:
        P[i] = P[i-1] + P[i]
    answer += P[i]
print(answer)