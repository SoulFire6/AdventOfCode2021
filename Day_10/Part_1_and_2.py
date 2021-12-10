def getScore(x,flag):
    values=[[1,3],[2,57],[3,1197],[4,25137]]
    delimiters=[")","]","}",">"]
    return values[delimiters.index(x)][flag]

def parseLine(string,isPart1):
    openChunk=["(","[","{","<"]
    closeChunk=[")","]","}",">"]
    delimiters=[]
    for x in string:
        if x in openChunk:
            delimiters.append(x)
        elif x in closeChunk:
            if delimiters[-1]==openChunk[closeChunk.index(x)]:
                del delimiters[-1]
            else:
                if isPart1:
                    return getScore(x,True)
                else:
                    return 0
    if isPart1:
        return 0
    else:
        return closeLine([closeChunk[openChunk.index(delimiters[i])] for i in range(0,len(delimiters))])

def closeLine(delimiterList):
    score=0
    for i in range(0,len(delimiterList)):
        score*=5
        score+=getScore(delimiterList[-1],False)
        del delimiterList[-1]
    return score

def findMiddleScore(listToSort):
    max=len(listToSort)
    for i in range(0,max-1):
        for j in range(0,max-i-1):
            if listToSort[j]>listToSort[j+1]:
                listToSort[j],listToSort[j+1]=listToSort[j+1],listToSort[j]
    return listToSort[int(max/2)]

#MAIN

result=0
scores=[]
with open("in.txt","r") as file:
    for line in file:
        result+=parseLine(line,True)
        score=parseLine(line,False)
        if score!=0:
            scores.append(score)
print(result)
print(findMiddleScore(scores))
