N = int(input())
len_road = list(map(int, input().split()))
Lit = list(map(int, input().split()))

#total_len = sum(len_road) - len_road[0]
#answer = len_road[0] * Lit[0]
#Lit.remove(Lit[len(Lit)-1])
#Lit.remove(Lit[0])
#Lit.sort()
#answer += Lit[0] * total_len

m = Lit[0]
answer = 0
for i in range(N-1):
    if Lit[i] < m:
        m = Lit[i]
    answer += m * len_road[i]

print(answer)