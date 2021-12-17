def initialiseQueue(amount)
  cave=File.read("in.txt").split("\n").map{|x| x.split('')}.map{|x| x.map{|y| y.to_i}}
  caveLen=cave.length
  l=caveLen*amount
  queue=[]
  qLen=l**2
  for i in 0..qLen-1
    row=i/l
    column=i%l
    queue.append([[row,column],Float::INFINITY,2*(l-1)-(row+column),(cave[row%caveLen][column%caveLen]+row/caveLen+column/caveLen)])#X,Y,Cost,Dist,CaveRisk
    if queue[i][3]>9
      queue[i][3]=queue[i][3]%9
    end
  end
  queue[0][1]=0
  return queue
end

# A* algorithm, returns the right values but runs very slow
# probably because it needs to find each adjacent cell by
# searching through all the queue with ruby's detect function
# (inside the function updateNode)

def findPath(queue,length,printQueue)
  if queue[0][0]==[length-1,length-1]
    print("found: ",queue[0],"\n")
    return queue[0][1]
  end
  if queue[0][0]!=[0][0]
    updateNode(queue,-1,0)
    updateNode(queue,0,-1)
  end
  if queue[0][0]!=[length-1,0] && queue[0][0]!=[0,length-1]
    updateNode(queue,1,0)
    updateNode(queue,0,1)
  end
  if printQueue
    print(queue[0],"\n")
  end
  queue.shift()
  queue.sort_by!{|x| [x[1],x[2]]}
  if queue[0]==nil
    return nil
  else
    findPath(queue,length,printQueue)
  end
end
def updateNode(queue,offsetX,offsetY)
  nextNode=queue.detect{|x| x.include?([queue[0][0][0]+offsetX,queue[0][0][1]+offsetY])}
  if nextNode
    if queue[0][1]+nextNode[3]<nextNode[1]
      nextNode[1]=queue[0][1]+nextNode[3]
    end
  end
end
print("Part 1 (y/n): ")
if (gets().include?"y")
  amount=1
else
  amount=5
end
print("Print queue (y/n): ")
if (gets().include?"y")
  flag=true
else
  amount=false
end
queue=initialiseQueue(amount)
l=Math.sqrt(queue.length)
print(findPath(queue,l,flag))
