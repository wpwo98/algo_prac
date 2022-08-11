N = int(input())
score = 0
for n in range(N):
    t_case = list(map(str, input()))
    flag = 0
    score = 0
    for i in range(len(t_case)):
        if t_case[i]=='O':
            flag += 1
        else :
            flag = 0
        score += flag
    print(score)