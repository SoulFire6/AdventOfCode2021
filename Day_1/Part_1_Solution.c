#include <stdio.h>
#include <string.h>
int main() {
	FILE *f;
	int value=0;
	int currVal=0;
	int count=0;
	f=fopen("in.txt", "r");
	if (f) {
		fscanf(f, "%d\n", &currVal);
		printf("Intial value %d\n", currVal);
		while(!feof(f)) {
			fscanf(f, "%d\n", &value);
			if (value>currVal) {
				count++;
				printf("(+) Increased to %d\n",value);
			} else {
				printf("(-) Decreased to %d\n",value);
			}
			currVal=value;
		}
		printf("\nIncreased %d times\n",count);
	} else {
		printf("Failed to open file\n");
	}
}
