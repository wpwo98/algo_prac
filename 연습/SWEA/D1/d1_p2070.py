T = int(input())
for i in range(1,T+1):
    t1, t2 = input().split()
    result = "#" + str(i)
    if int(t1) == int(t2):
        result += " ="
    elif int(t1) > int(t2):
        result += " >"
    else:
        result += " <"
    print(result)