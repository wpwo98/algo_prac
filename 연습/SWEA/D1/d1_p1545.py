N = int(input())
result = ""
for i in range(N,-1,-1):
    result += str(i) + " "
result = result[:-1]
print(result)