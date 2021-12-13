def fold(coords,command)
  pos,value=command
  coords.each_with_index do |coord,index|
    if coord[0].to_i>value.to_i and pos=="x"
        coords[index]=[2*value.to_i-coord[0].to_i,coord[1].to_i]
    elsif coord[1].to_i>value.to_i and pos=="y"
        coords[index]=[coord[0].to_i,2*value.to_i-coord[1].to_i]
    end
  end
end

def printPaper(coords,flag)
  print("\nAfter completing all the folds, you get the eight letter code:\n\n")
  maxColumn,maxRow=coords.max_by{|x,y| [x,y]}
  for j in 0..maxRow
    for i in 0..maxColumn
      if coords.include?([i,j])
        print('#')
      else
        if flag
          print('.')
        else
          print(' ')
        end
      end
    end
    print("\n")
  end
  print("\n")
end

#Main

fileData=File.read("in.txt").split("\n\n")
coords=fileData[0].split.map{|x| x.split(',')}.map{|x,y| [x.to_i,y.to_i]}
commands=fileData[1].split.select{|x| x.include?('x') || x.include?('y')}.map{|x| x.split("=")}
commands.each_with_index do |command,index|
  fold(coords,command)
  if index==0
    print("After one fold there are ",coords.uniq.count," marks\n\n")
  end
end
print("Display unmarked cells on the paper (y/n)?: ")
printPaper(coords,gets.include?('y'))
