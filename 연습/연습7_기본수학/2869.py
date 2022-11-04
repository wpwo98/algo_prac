A, B, V = map(int,input().split())

H = V-A
if H % (A-B) == 0 :
    day = int(H/(A-B))+ 1
else:
    day = int(H/(A-B)) + 2

print(day)