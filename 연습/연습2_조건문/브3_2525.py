A, B = map(int, input().split())
C = int(input())

if (B+C)<60 :
    print(A, B+C)
    
elif A+int((B+C)/60) >= 24 :
    print(A+int((B+C)/60) - 24, B+C-int((B+C)/60)*60)
else: print(A+int((B+C)/60), B+C-int((B+C)/60)*60)