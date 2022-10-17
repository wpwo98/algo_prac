S = input().split('-')
ans = 0
for i in S[0].split('+'):
    ans += int(i)
for i in S[1:]:
    for j in i.split('+'):
        ans -= int(j)
print(ans)