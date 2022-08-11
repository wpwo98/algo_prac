N = []
N_i = 0
for i in range(10):
    n = int(input())
    if n%42 in N :
        continue
    else :
        N.append(n%42)
        N_i += 1
print(N_i)