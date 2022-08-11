Z = [0,0,0,0,0,0,0,0,0]
max_i = 0
max_v = 0
for i in range(0,9):
    Z[i] = int(input())
    if Z[i] > max_v :
        max_v = Z[i]
        max_i = i+1
    #print("max_v:",max_v,"max_i:",max_i)
print(max_v)
print(max_i)