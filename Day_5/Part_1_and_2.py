def updateMatrix(matrix,start,end,flag):
    if start[0]==end[0]:
        for i in range(min(start[1],end[1]),max(start[1],end[1])+1):
            matrix[i][start[0]]+=1
    elif start[1]==end[1]:
        for i in range(min(start[0],end[0]),max(start[0],end[0])+1):
            matrix[start[1]][i]+=1
    else:
        if flag:
            for i in range(0,abs(end[0]-start[0])+1):
                if start[0]<end[0]:
                    if start[1]<end[1]:
                        matrix[start[1]+i][start[0]+i]+=1
                    else:
                        matrix[start[1]-i][start[0]+i]+=1
                else:
                    if start[1]<end[1]:
                        matrix[start[1]+i][start[0]-i]+=1
                    else:
                        matrix[start[1]-i][start[0]-i]+=1

def count(matrix):
    count=0
    for x in matrix:
        for y in x:
            if y>1:
                count+=1
    return count
startList=[]
endList=[]
with open("in.txt","r") as file:
  for line in file:
      start,end=line.strip().split(" -> ")
      startList.append([int(x) for x in start.split(',')])
      endList.append([int(x) for x in end.split(',')])

maxRow=0
maxColumn=0

for i in range(0,len(startList)):
    for x in startList[i]:
        if x>maxRow:
            maxRow=x
    for x in endList[i]:
        if x>maxColumn:
            maxColumn=x

lineMatrix=[[0 for x in range(0,maxRow+1)] for y in range(0,maxColumn+1)]
diagonalFlag=True if input("Consider diagonal lines? (y/n)")=='y' else False
for i in range(0,len(startList)):
    updateMatrix(lineMatrix,startList[i],endList[i],diagonalFlag)
print(count(lineMatrix))
