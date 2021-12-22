def turn(player,die,rolls):
    move=0
    for i in range(0,3):
        move+=die
        rolls+=1
        die=1 if die==100 else die+1
    player[0]=10 if (player[0]+move)%10==0 else (player[0]+move)%10
    player[1]+=player[0]
    return die,rolls

def Part1(p1Pos,p2Pos):
    p1=[p1Pos,0]
    p2=[p2Pos,0]
    die=1
    rolls=0
    while (True):
        die,rolls=turn(p1,die,rolls)
        if p1[1]>999:
            break
        die,rolls=turn(p2,die,rolls)
        if p2[1]>999:
            break
    if p1[1]>p2[1]:
        print("\nDeterministic Dirac Dice result: ",p2[1]*rolls)
    else:
        print("\nDeterministic Dirac Dice result: ",p1[1]*rolls)

def quantumTurn(p1Pos,p1Score,p2Pos,p2Score,move,rolls,isP1Turn,wins):
    possibilites=[[3, 1], [4, 3], [5, 6], [6, 7], [7, 6], [8, 3], [9, 1]] #Calculated using ruby script
    if isP1Turn:
        p1Pos=10 if (p1Pos+move)%10==0 else (p1Pos+move)%10
        p1Score+=p1Pos
        if p1Score>20:
            return 1
        isP1Turn=not isP1Turn
    else:
        p2Pos=10 if (p2Pos+move)%10==0 else (p2Pos+move)%10
        p2Score+=p2Pos
        if p2Score>20:
            return 0
        isP1Turn=not isP1Turn
    wins=0
    for x in possibilites:
        wins+=x[1]*quantumTurn(p1Pos,p1Score,p2Pos,p2Score,x[0],rolls+3,isP1Turn,wins)
    return wins

def Part2(p1Pos,p2Pos):
    possibilites=[[3, 1], [4, 3], [5, 6], [6, 7], [7, 6], [8, 3], [9, 1]]
    result=0
    print("\n\nCalculating quantum results")
    for i,x in enumerate(possibilites):
        result+=x[1]*quantumTurn(p1Pos,0,p2Pos,0,x[0],3,True,0)
        print(i+1,"/",len(possibilites))
    print("\nQuantum Dirac Dice result: ",result)

#MAIN

fileInput=[x.rstrip().split(':') for x in open("in.txt").readlines()]
Part1(int(fileInput[0][1]),int(fileInput[1][1]))
Part2(int(fileInput[0][1]),int(fileInput[1][1]))
