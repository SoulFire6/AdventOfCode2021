def filterResults(position,valueList,flag):
    result=valueList[:]
    value=calcMostCommonBit(position,result,flag)
    for item in valueList:
        if item[position]!=value and item in result:
            if len(result)>1:
                result.remove(item)
            else:
                return int(result[0],2)
    if len(result)==1:
        return int(result[0],2)
    else:
        return filterResults(position+1,result,flag)

def calcMostCommonBit(position,list,flag):
    count=0
    for x in list:
        if x[position]=="1":
            count+=1
        else:
            count-=1
    if count>=0:
        count=True
    else:
        count=False
    if flag:
        count=not count
    return "1" if count else "0"

#MAIN

gamma=""
epsilon=""
binaryList=[]

with open("in.txt","r") as file:
    for line in file:
        binaryList.append(line.rstrip())
solution=[0 for i in range(len(binaryList[0]))]

#PART 1
for i in range(0,len(binaryList[0])):
    gamma+=calcMostCommonBit(i,binaryList,False)
    epsilon+=calcMostCommonBit(i,binaryList,True)
res=str(int(gamma,2)*int(epsilon,2))

#PART 2
oxygenRating=filterResults(0,binaryList,False)
lifeSupportRating=filterResults(0,binaryList,True)
res2=str(oxygenRating*lifeSupportRating)

print("Part 1 result: "+res)
print("Part 2 result: "+res2)
