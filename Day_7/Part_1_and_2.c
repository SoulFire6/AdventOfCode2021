#include <stdio.h>
#include <stdlib.h>
int fuelCost (int pos[], int size, int x, int minFuel) {
  int cost=0;
  for (int i=0;i<size;i++) {
    cost+=abs(pos[i]-x);
    if (cost>minFuel) {
      return minFuel;
    }
  }
  return cost;
}
int fuelCost2 (int pos[], int size, int x, int minFuel) {
  int cost=0;
  for (int i=0;i<size;i++) {
    for (int j=1; j<abs(pos[i]-x)+1; j++) {
      cost+=j;
      if (cost>minFuel) {
        return minFuel;
      }
    }
  }
  return cost;
}
int main() {
  FILE *f;
  int n=1000;
  int pos[n];
  int minFuel,minFuel2,max;
  f=fopen("in.txt","r");
  if (f) {
    minFuel=0;
    max=0;
    for (int i=0; i<n; i++) {
      fscanf(f,"%d",&pos[i]);
      fscanf(f,",");
      minFuel+=pos[i];
      if (pos[i]>max) {
        max=pos[i];
      }
    }
    fclose(f);
    minFuel2=minFuel*minFuel;
    for (int i=0; i<max; i++) {
      minFuel=fuelCost(pos,n,i,minFuel);
      minFuel2=fuelCost2(pos,n,i,minFuel2);
    }
    printf("Result part 1: %d\n",minFuel);
    printf("Result part 2: %d\n",minFuel2);
  } else {
    printf("Error opening file\n");
  }
}
