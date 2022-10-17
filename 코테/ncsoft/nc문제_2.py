
music = [10,9,4,5,12]
answer = 0
result = 0
white = [1,3,5,7,8,10,12]
black = [2,4,6,9,11]

location = 1
for i in range(len(music)):
    leng = abs(music[i] - location)
    if (music[i] in white) and (location in white):
        leng /= 2.0
        leng += 0.5
        print(int(leng))
        answer += int(leng)
        
    
    elif (music[i] in black) and (location in black):

        if leng % 2 == 0:
            leng /= 2
            leng += 1
            answer += leng
            print(leng)
        else :
            leng /= 2.0
            leng += 1.5
            answer += int(leng)
            print(leng)        

    else:
        if leng % 2 == 0:
            leng /= 2
            leng += 1
            answer += leng
            print(leng)
        else :
            leng /= 2.0
            leng += 0.5
            answer += int(leng)
            print(leng)
    location = music[i]
    
answer = int(answer)
print(answer)