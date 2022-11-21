T = int(input())
for t in range(T):
    result = ""
    list_t = list(map(int,input().split()))
    avg_t = round(sum(list_t) / 10)
    result = "#" + str(t+1) + " " + str(avg_t)
    print(result)
