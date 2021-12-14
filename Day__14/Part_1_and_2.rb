def countLetters(letters,string)
  result=letters.map{|x| [x,0]}
  for i in 0..string.length-1
    result.detect{|x| x.include?(string[i])}[1]+=1
  end
  return result
end

def replacePairs(letters,pairCount,replacements,currentIndex,maxIndex)
  pairs=pairCount.map{|x| [x[0],0]}
  pairCount.each do |value|
    if value[1]>0
        replacements.each do |replace|
          if value[0]==replace[0]
            letters.detect{|x| x.include?(replace[1])}[1]+=value[1]
            [value[0][0]+replace[1],replace[1]+value[0][1]].each do |pair|
              pairs.detect{|x| x.include?(pair)}[1]+=value[1]
            end
          end
        end
    end
  end
  if currentIndex==maxIndex
    letters=letters.sort_by{|x| x[1]}
    return (letters[-1][1]-letters[0][1])
  else
    return replacePairs(letters,pairs,replacements,currentIndex+1,maxIndex)
  end
end

fileData=File.read("in.txt").split("\n\n")
polymer=fileData[0]
replacements=fileData[1].split("\n").map{|x| x.split(" -> ")}
possiblePairs=fileData[1].split("\n").map{|x| x.split(" -> ")}.map{|x| [x[0].split('').join,0]}.uniq
letters=possiblePairs.map{|x| x[0].split('')}.join.split('').uniq

for i in 0..polymer.length-1
  possiblePairs.each do |value|
    if value[0]==polymer[i..i+1]
      value[1]+=1
    end
  end
end

print("After 10 replacements: ",replacePairs(countLetters(letters,polymer),possiblePairs,replacements,1,10),"\n")
print("After 40 replacements: ",replacePairs(countLetters(letters,polymer),possiblePairs,replacements,1,40),"\n")
