def checkBingo(board)
  board.each_with_index do |row|
    if row.uniq.count == 1
      return calcScore(board)
    end
  end
  for i in 0..4 do
    won=true
    for j in 0..4 do
      if(board[j][i])!="X"
        won=false
        break
      end
    end
    if won
      return calcScore(board)
    end
  end
  if won
    return calcScore(board)
  end
  return -1
end

def calcScore(board)
  sum=0
  for i in 0..4 do
    for j in 0..4 do
      if board[i][j]!='X'
        sum+=board[i][j].to_i
      end
    end
  end
  return sum
end

fileData=File.read("in.txt").split
numbSequence=fileData[0].split(',')
boards=[]
count=1
while count<fileData.length do
  newBoard=Array.new(5){Array.new(5,-1)}
  for i in 0..4 do
    for j in count..count+4 do
      newBoard[i][(j-1)%5]=fileData[j]
    end
    count+=5
  end
  boards.append(newBoard)
end

winningBoards=[]
winningScores=[]
result=-1
for i in 0..numbSequence.length-1 do
  boards.each do |board|
    board.each{|row| row.include?(numbSequence[i])? row[row.index(numbSequence[i])]='X' : false}
  end
  boards.each_with_index do |board,boardIndex|
    result=checkBingo(board)
    if result!=-1 and not winningBoards.include?(boardIndex)
      winningBoards.append(boardIndex)
      winningScores.append(result*numbSequence[i].to_i)
    end
  end
end
print("First board to win is ",winningBoards[0]," with a score of: ",winningScores[0],"\n")
print("Last board to win is ",winningBoards[-1]," with a score of: ",winningScores[-1])
