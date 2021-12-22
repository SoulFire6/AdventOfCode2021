results=[]
[1,2,3].repeated_permutation(3).to_a.map{|x| results.append(x[0]+x[1]+x[2])}
possibilities=results.uniq.sort_by{|x| x}.map{|x| [x,0]}
results.each do |x|
  possibilities.detect{|y| y[0]==x}[1]+=1
end
print(possibilities)
