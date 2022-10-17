paper = [7,3,5,-2,9]
n = 2
answer = 0
max = 0

for i in range(n):
    print(i)
    for j in range(len(paper)):
        print("j=",paper[j])
        for k in range(j+1, len(paper), 2):
            print("k=",paper[k])
            if paper[j] + paper[k] > max :
                max = paper[j] + paper[k]
    print()

print (max)