import java.util.*;
public class Part_1_and_2{
  public static void main(String[] args){
    Integer[] input = {5,1,5,3,2,2,3,1,1,4,2,4,1,2,1,4,1,1,5,3,5,1,5,3,1,2,4,4,1,1,3,1,1,3,1,1,5,1,5,4,5,4,5,1,3,2,4,3,5,3,5,4,3,1,4,3,1,1,1,4,5,1,1,1,2,1,2,1,1,4,1,4,1,1,3,3,2,2,4,2,1,1,5,3,1,3,1,1,4,3,3,3,1,5,2,3,1,3,1,5,2,2,1,2,1,1,1,3,4,1,1,1,5,4,1,1,1,4,4,2,1,5,4,3,1,2,5,1,1,1,1,2,1,5,5,1,1,1,1,3,1,4,1,3,1,5,1,1,1,5,5,1,4,5,4,5,4,3,3,1,3,1,1,5,5,5,5,1,2,5,4,1,1,1,2,2,1,3,1,1,2,4,2,2,2,1,1,2,2,1,5,2,1,1,2,1,3,1,3,2,2,4,3,1,2,4,5,2,1,4,5,4,2,1,1,1,5,4,1,1,4,1,4,3,1,2,5,2,4,1,1,5,1,5,4,1,1,4,1,1,5,5,1,5,4,2,5,2,5,4,1,1,4,1,2,4,1,2,2,2,1,1,1,5,5,1,2,5,1,3,4,1,1,1,1,5,3,4,1,1,2,1,1,3,5,5,2,3,5,1,1,1,5,4,3,4,2,2,1,3};
    Part1(input,80);
    Part2(input,256);
  }

  private static void Part1 (Integer[] array, int days) {
    int count;
    List<Integer> fishList=new ArrayList<Integer>();
    for (Integer item:array) {
      fishList.add(item);
    }
    for (int i=0;i<days;i++) {
      count=0;
      for (int j=0;j<fishList.size();j++) {
        fishList.set(j,(fishList.get(j))-1);
        if (fishList.get(j)<0) {
          fishList.set(j,6);
          count++;
        }
      }
      for (int j=0;j<count;j++) {
        fishList.add(8);
      }
    }
    System.out.print("Result part 1: ");
    System.out.println(fishList.size());
  }

  private static void Part2 (Integer[] array, int days) {
    Long[] fishList={0L,0L,0L,0L,0L,0L,0L,0L,0L};
    Long newFish=0L;
    Long result=0L;
    for (int i=0; i<array.length;i++) {
      fishList[array[i]]+=1;
    }
    for (int day=0; day<days; day++) {
      newFish=fishList[0];
      for (int i=0; i<fishList.length-1; i++) {
        fishList[i]=fishList[i+1];
      }
      fishList[6]+=newFish;
      fishList[8]=newFish;
    }
    for (Long fish:fishList) {
      result+=fish;
    }
    System.out.print("Result part 2: ");
    System.out.println(result);
  }
}
