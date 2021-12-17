$headerCount=0
$hexBinary={
  "0"=>"0000",
  "1"=>"0001",
  "2"=>"0010",
  "3"=>"0011",
  "4"=>"0100",
  "5"=>"0101",
  "6"=>"0110",
  "7"=>"0111",
  "8"=>"1000",
  "9"=>"1001",
  "A"=>"1010",
  "B"=>"1011",
  "C"=>"1100",
  "D"=>"1101",
  "E"=>"1110",
  "F"=>"1111"
}
def hexToBinary(hexCode)
  result=""
  hexCode.split('').each do |x|
    result+=$hexBinary[x]
  end
  return result
end

def parsePacket(header,typeID,packet)
  $headerCount+=header.to_i
  if typeID==4
    #VALUE
    result=""
    while true
      result+=packet[1..4]
      value=packet[0]
      packet=packet[5..]
      if value=="0"
        return packet,result.to_i(2)
      end
    end
  else
    values=[]
    lenTypeID=packet[0]
    packetLength=packet[1..15].to_i(2)
    packetNum=packet[1..11].to_i(2)
    if typeID==5 || typeID==6 || typeID==7
      packetNum=2
    end
    if lenTypeID=="0"
      packet=packet[16..]
      while(packet!=nil && packetLength>0)
        length=packet.length
        packet,value=parsePacket(packet[0..2].to_i(2),packet[3..5].to_i(2),packet[6..])
        values.append(value)
        packetLength-=(length-packet.length)
      end
    else
      packet=packet[12..]
      for i in 1..packetNum
        packet,value=parsePacket(packet[0..2].to_i(2),packet[3..5].to_i(2),packet[6..])
        values.append(value)
      end
    end
  end
  if typeID==0
    #SUM
    result=0
    values.each do |x|
      result+=x
    end
    return packet,result
  elsif typeID==1
    #PRODUCT
    result=1
    values.each do |x|
      result*=x
    end
    return packet,result
  elsif typeID==2
    #MIN
    result=values[0]
    values.each do |x|
      if x<result
        result=x
      end
    end
    return packet,result
  elsif typeID==3
    #MAX
    result=values[0]
    values.each do |x|
      if x>result
        result=x
      end
    end
    return packet,result
  elsif typeID==5
    #GREATER THAN
    if values[0]>values[1]
      result=1
    else
      result=0
    end
    return packet,result
  elsif typeID==6
    #LESS THAN
    if values[0]<values[1]
      result=1
    else
      result=0
    end
    return packet,result
  elsif typeID==7
    #EQUALS
    if values[0]==values[1]
      result=1
    else
      result=0
    end
    return packet,result
  else
    puts("ERROR")
    return nil
  end
end

#MAIN

result=hexToBinary(File.read("in.txt").rstrip())
packet,result=parsePacket(result[0..2].to_i(2),result[3..5].to_i(2),result[6..])
print("Total header count: ",$headerCount,"\n")
print("Result: ",result,"\n")
