N = int(input())
s = list(map(int, input().split()))
s_max = max(s)
score = 0
for n in range(N):
    score += s[n]/s_max*100
s_i = round(score/len(s),6)
print(s_i)