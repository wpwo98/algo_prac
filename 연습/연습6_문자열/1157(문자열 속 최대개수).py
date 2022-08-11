Alpha = input().upper()
Alpha_set = list(set(Alpha))
cnt_list = []
for a in Alpha_set :
    cnt = Alpha.count(a)
    cnt_list.append(cnt)
if cnt_list.count(max(cnt_list)) > 1 :
    print("?")
else:
    print(Alpha_set[cnt_list.index(max(cnt_list))])