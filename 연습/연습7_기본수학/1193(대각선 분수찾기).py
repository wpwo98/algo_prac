N = int(input())
line = 0
max_N = 0

# 1 3 6 10 15 ... line과 line별 최대 수 확인
while N > max_N:
    line += 1
    max_N += line

gap = max_N - N
# 짝수
if line % 2 == 0:
    top = line - gap
    bottom = gap + 1
# 홀수
else:
    top = gap + 1
    bottom = line - gap
answer = ""
answer += str(top) + "/" + str(bottom)
print(answer)