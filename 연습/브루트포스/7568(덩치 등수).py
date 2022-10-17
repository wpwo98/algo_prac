N = int(input())
total = []
for i in range(N):
    x, y = map(int, input().split())
    total.append((x,y))
for i in total:
    rank = 1
    for j in total:
        if i[0] < j[0] and i[1] < j[1] :
            rank += 1
    print(rank, end=" ")