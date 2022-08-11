C = int(input())
for c in range(C):
    stu_score = list(map(int, input().split()))
    stu_sum = sum(stu_score) - stu_score[0]
    #print("stu_sum =",stu_sum)
    stu_avg = stu_sum / (len(stu_score)-1)
    #print("stu_avg =",stu_avg)
    stu_pass = 0
    for stu_s in range(1, len(stu_score)):
        if stu_score[stu_s] > stu_avg :
            stu_pass += 1
    stu_pro = (stu_pass / (len(stu_score)-1) ) * 100
    stu_result = str('%.3f'%stu_pro) + "%"
    print(stu_result)