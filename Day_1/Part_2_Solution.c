#include <stdio.h>
#include <string.h>
int sum(int a, int b, int c);
int main() {
	FILE *f;
	int currVal[3]={0,0,0};
	int value[3]={0,0,0};
	int sumValue[2]={0,0};
	int count=0;
	f=fopen("in.txt", "r");
	if (f) {
		fscanf(f, "%d\n", &currVal[0]);
		fscanf(f, "%d\n", &currVal[1]);
		fscanf(f, "%d\n", &currVal[2]);
		value[0]=currVal[1];
		value[1]=currVal[2];
		printf("Intial value %d\n", sum(currVal[0],currVal[1],currVal[2]));
		while(!feof(f)) {
			fscanf(f, "%d\n", &value[2]);
			sumValue[0]=sum(value[0],value[1],value[2]);
			sumValue[1]=sum(currVal[0],currVal[1],currVal[2]);
			if (sumValue[0]>sumValue[1]) {
				count++;
				printf("(+) Increased to %d\n",sumValue[0]);
			} else {
				printf("(-) Decreased to %d\n",sumValue[0]);
			}
			currVal[0]=value[0];
			currVal[1]=value[1];
			currVal[2]=value[2];
			value[0]=value[1];
			value[1]=value[2];
		}
		printf("\nIncreased %d times\n",count);
	} else {
		printf("Failed to open file\n");
	}
}
int sum(int a, int b, int c) {
	return a+b+c;
}
