destinations=dict()

def getPath(path,maxNum):
    result=0
    if path[-1] in destinations:
        for x in destinations[path[-1]]:
            if x=="end":
                result+=1
            else:
                if x.islower() and x in path:
                    if countOccurences(path,x)<maxNum+1:
                        result+=getPath(path+[x],maxNum-1)
                    else:
                        pass
                else:
                    result+=getPath(path+[x],maxNum)
    return result

def countOccurences(array,item):
    count=0
    for x in array:
        if x==item:
            count+=1
    return count


with open("in.txt","r") as file:
    for line in file:
        start,end=line.rstrip().split('-')
        if end!="start":
            if start in destinations:
                destinations[start].append(end)
            else:
                destinations[start]=[end]
        if start!="start":
            if end in destinations:
                destinations[end].append(start)
            else:
                destinations[end]=[start]
if "end" in destinations:
    del destinations["end"]
print("Number of paths without returning to a small cave: ",getPath(["start"],0))
print("Number of paths with one return only to a small cave: ",getPath(["start"],1))



#Progress through parallel branches by checking destinations of each node and going through every options
#if islower() check if already present first, if end pass over that one
