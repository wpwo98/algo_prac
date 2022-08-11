T = int(input())
for t in range(T):
    R, S = input().split()
    text = ""
    for i in S:
        text += i * int(R)
    print(text)