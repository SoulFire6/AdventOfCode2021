def checkLowPoint(map,row,column)
  if row>0
    if map[row-1][column]<=map[row][column]
      return false
    end
  end
  if row<map.length-1
    if map[row+1][column]<=map[row][column]
      return false
    end
  end
  if column>0
    if map[row][column-1]<=map[row][column]
      return false
    end
  end
  if column<map[0].length-1
    if map[row][column+1]<=map[row][column]
      return false
    end
  end
  return true
end

def findBasin(map,row,column,basinValues)
  if not basinValues.include?([row,column]) and not map[row][column]=="9"
    basinValues.append([row,column])
  end
  if row>0
    if map[row-1][column]>map[row][column]
      findBasin(map,row-1,column,basinValues)
    end
  end
  if row<map.length-1
    if map[row+1][column]>map[row][column]
      findBasin(map,row+1,column,basinValues)
    end
  end
  if column>0
    if map[row][column-1]>map[row][column]
      findBasin(map,row,column-1,basinValues)
    end
  end
  if column<map[0].length-1
    if map[row][column+1]>map[row][column]
      findBasin(map,row,column+1,basinValues)
    end
  end
  return basinValues
end

def multiplyBasins(basins)
  basins = basins.sort_by {|x,y| x}.reverse
  return basins[0].to_i*basins[1].to_i*basins[2].to_i
end

lowPoints=0
basins=[]
fileData=File.read("in.txt").split
for i in 0..fileData.length-1 do
  for j in 0..fileData[0].length-1 do
    if checkLowPoint(fileData,i,j)
      lowPoints+=(1+fileData[i][j].to_i)
      basins.append(findBasin(fileData,i,j,[]).length)
    end
  end
end
print("Number of lowpoints: ",lowPoints,"\n")
print("Three largest basins multiplied: ",multiplyBasins(basins))
