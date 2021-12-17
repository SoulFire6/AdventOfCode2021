fileData=File.read("in.txt").rstrip().split.select{|x| x.include?("x") || x.include?("y")}
$targetX=fileData.detect{|x| x.include?("x")}[2..].split('..').map{|x| x.to_i}
$targetY=fileData.detect{|x| x.include?("y")}[2..].split('..').map{|x| x.to_i}
$velocityList=[]
$bestY=0

def step(position,velocity)
  position[0]+=velocity[0]
  position[1]+=velocity[1]
  if velocity[0]>0
    velocity[0]-=1
  elsif velocity[0]<0
    velocity[0]+=1
  end
  velocity[1]-=1
  return position,velocity
end

def checkTrajectory(velocity)
  initialVelocity=velocity.dup
  position=[0,0]
  maxY=0
  while (true)
    position,velocity=step(position,velocity)
    if position[1]>maxY
      maxY=position[1]
    end
    if (velocity[0]>0 && position[0]>$targetX[1]) || (velocity[0]<0 && position[0]<$targetX[0]) || position[1]<$targetY[0]
      return nil
    end
    if position[0]>=$targetX[0] && position[0]<=$targetX[1] && position[1]>=$targetY[0] && position[1]<=$targetY[1]
    #ENTERED TARGET AREA
      if maxY>$bestY
        $bestY=maxY
      end
      if not $velocityList.include?(initialVelocity)
        $velocityList.append(initialVelocity)
      end
      return nil
    end
  end
end

#MAIN
count=0
 for i in 0..$targetX[1]
   for j in 0..-$targetY[0]
    checkTrajectory([i,j])
    checkTrajectory([i,-j])
  end
end
print("Highest y of trajectories that enter target area: ",$bestY,"\n")
print("Number of distinct trajectories that enter the target area: ",$velocityList.length,"\n")
