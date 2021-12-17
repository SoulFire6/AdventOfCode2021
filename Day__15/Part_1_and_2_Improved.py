import math
class CaveArea:
  def __init__(self,risk,dist):
      self.risk=risk
      self.dist=dist
      self.cost=math.inf
      self.right=None
      self.down=None
      self.left=None
      self.up=None

def convertMatrixToNodeTree(matrix):
    queue=[]
    createdHead=False
    for i,matrixRow in enumerate(matrix):
        if createdHead:
            row.down=CaveArea(matrixRow[0],2*(len(matrix)-1)-(i+1))
            row.down.up=row
            row=row.down
            queue.append(row)
        else:
            head=CaveArea(matrixRow[0],2*(len(matrix)-1))
            createdHead=True
            head.cost=0
            queue.append(head)
            row=head
        curr=row
        for j,x in enumerate(matrixRow):
            if j>0:
                curr.right=CaveArea(x,2*(len(matrix)-1)-(i+j))
                curr.right.left=curr
                curr=curr.right
                queue.append(curr)
    linkNodeTree(head)
    return head,queue

def linkNodeTree(head):
    row=head
    curr=head
    while row.down!=None:
        curr=row
        while curr.right!=None:
            curr.right.down=curr.down.right
            curr.right.down.up=curr.right
            curr=curr.right
        row=row.down

# def printNodes(head):
#     row=head
#     curr=head
#     while row!=None:
#         curr=row
#         string=""
#         while curr!=None:
#             string+=str(curr.risk)
#             curr=curr.right
#         print(string)
#         row=row.down

def updateNodeCost(queue):
    curr=queue[0]
    if curr.right!=None:
        if curr.cost+curr.right.risk<curr.right.cost:
            curr.right.cost=curr.cost+curr.right.risk
            sortQueue(queue,curr.right)
    if curr.down!=None:
        if curr.cost+curr.down.risk<curr.down.cost:
            curr.down.cost=curr.cost+curr.down.risk
            sortQueue(queue,curr.down)

    if curr.left!=None:
        if curr.cost+curr.left.risk<curr.left.cost:
            curr.left.cost=curr.cost+curr.left.risk
            sortQueue(queue,curr.left)
    if curr.up!=None:
        if curr.cost+curr.up.risk<curr.up.cost:
            curr.up.cost=curr.cost+curr.up.risk
            sortQueue(queue,curr.up)

def sortQueue(queueToSort,elementToFind):
    queueToSort.remove(elementToFind)
    for i,x in enumerate(queueToSort):
        if x.cost>elementToFind.cost:
            queueToSort.insert(i,elementToFind)
            break
        elif x.cost==elementToFind.cost and x.dist>elementToFind.dist:
            queueToSort.insert(i,elementToFind)
            break

def findPath(queue):
    if (queue[0].right==None and queue[0].down==None) or len(queue)==1:
        return queue[0].cost
    updateNodeCost(queue)
    queue.pop(0)
    return queue

def expandMatrix(matrix,amount):
    return [[x+i+j if x+i+j<10 else ((x+i+j)%10)+1 for i in range(amount) for x in row] for j in range(amount) for row in matrix]

#MAIN

nodeMatrix=[]
with open("in.txt","r") as file:
    for line in file:
        nodeMatrix.append([int(x) for x in line.rstrip()])
amount=1 if "y" in input("Part 1 (y/n): ") else 5
printDistances=True if "y" in input("Print current distances for each iteration?") else False
nodeMatrix=expandMatrix(nodeMatrix,amount)
head,queue=convertMatrixToNodeTree(nodeMatrix)
result=findPath(queue)
count=0
while isinstance(result, list):
    if printDistances:
        print("Iteration: ",count,"| Distance:  ",result[0].dist)
        count+=1
    result=findPath(result)
print("Result: ",result)
