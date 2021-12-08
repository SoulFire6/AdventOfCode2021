def Part1(string):
    count=0
    values=[x for x in string.rstrip().split(" | ")]
    for x in values[1].split(" "):
        if len(x)==2 or len(x)==3 or len(x)==4 or len(x)==7:
            count+=1
    return count
    
def Part2(string):
    result=""
    values=[x for x in string.rstrip().split(" | ")]
    cypher=determineCypher(values[0])
    for x in values[1].split(" "):
        for character in cypher:
            found=True
            if len(character[1])==len(x):
                for letter in character[1]:
                    if letter not in x:
                        found=False
                        break
                if found:
                    result+=str(character[0])
    return(int(result))

def determineCypher(codedString):
    # 1,4,7 and 8 can be found just by length
    cypher=[[0,""],[1,""],[2,""],[3,""],[4,""],[5,""],[6,""],[7,""],[8,""],[9,""]]
    # the three with length five are 2,3,5
    fives=[]
    # the three with length six are 0,6,9
    sixes=[]
    for x in codedString.split(" "):
        if len(x)==2:
            #1 is the only one with length 2
            cypher[1][1]=x
        elif len(x)==3:
            #7 is the only one with length 3
            cypher[7][1]=x
        elif len(x)==4:
            #4 is the only one with length 4
            cypher[4][1]=x
        elif len(x)==7:
            #8 is the only one with length 8
            cypher[8][1]=x
        elif len(x)==5:
            #2,3 and 5 all have length 5
            fives.append(x)
        elif len(x)==6:
            #0,6 and 9 all have length 6
            sixes.append(x)

    # Now to work out the fives
    for x in list(fives):
        #3 is the only one with both characters of 1
        count=0
        for letter in cypher[1][1]:
            if letter in x:
                count+=1
        if count==2:
            cypher[3][1]=x
        else:
            #5 has 3 characters from 4, 2 has 2
            count=0
            for letter in cypher[4][1]:
                if letter in x:
                    count+=1
            if count==3:
                cypher[5][1]=x
            else:
                #the last one remaining must be 2
                cypher[2][1]=x
    # Now to work out the sixes
    for x in list(sixes):
        #6 is the only one with only one character from 1, 0 and 9 have both of them
        count=0
        for letter in cypher[1][1]:
            if letter in x:
                count+=1
        if count==1:
            cypher[6][1]=x
        else:
            #9 is the only one with all the characters from 4
            count=0
            for letter in cypher[4][1]:
                if letter in x:
                    count+=1
            if count==4:
                cypher[9][1]=x
            else:
                #the last one remaining must be 0
                cypher[0][1]=x
    return cypher

#MAIN
result=[0,0]
with open("in.txt","r") as file:
    for line in file:
        result[0]+=Part1(line)
        result[1]+=Part2(line)

print("Result of part 1: ",result[0])
print("Result of part 2: ",result[1])
