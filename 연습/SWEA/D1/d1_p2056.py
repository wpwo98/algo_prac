T = int(input())
for i in range(1,T+1):
    date = str(input())
    t = int(date)
    flag = 0
    year = date[:4]
    str_m = date[4:6]
    str_d = date[6:]
    month = (t % 10000) // 100
    day = t % 100

    if month in [1,3,5,7,8,10,12]:
        if day < 1 or day > 31:
            flag = 1
    elif month in [4,6,9,11]:
        if day < 1 or day > 30:
            flag = 1
    elif month == 2:
        if day < 1 or day > 28:
            flag = 1
    else:
        flag = 1

    if flag == 0 :
        result = "#" + str(i) + " " + year + "/" + str_m + "/" + str_d
        print(result)
    else:
        result = "#" + str(i) + " -1"
        print(result)