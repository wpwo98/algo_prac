n, m = map(int, input().split())
W = input()
S = input()
answer = 0
Wa = [0]*58
Sa = [0]*58
start, length = 0, 0

for x in W:
    Wa[ord(x) - 65] += 1        # 문자를 아스키 코드로.

for i in range(m):
    Sa[ord(S[i]) - 65] += 1
    length += 1

    if length == n:
        if Wa == Sa:
            answer += 1
        Sa[ord(S[start]) - 65] -= 1
        start += 1
        length -= 1

print(answer)