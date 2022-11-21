N = int(input())
score_N = list(map(int,input().split()))
score_N.sort()
ind = N // 2
result = score_N[ind]
print(result)