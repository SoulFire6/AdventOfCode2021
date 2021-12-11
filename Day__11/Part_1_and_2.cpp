#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int step(int **board, int size);
void flash(int **board, int size, int row, int column);
bool checkBoard(int **board, int size);

int main() {
  ifstream file;
  char element;
  int size=10;
  int result,count,value;
  int **board;

  board=new int *[10];
  for (int i=0; i<size; i++) {
    board[i]=new int[10];
  }

  file.open("in.txt");
  if (file.is_open()) {
    for (int i=0; i<size; i++) {
      for (int j=0; j<size; j++) {
        do {
          file.get(element);
        } while (!isdigit(int(element)));
        board[i][j]=int(element-'0');
      }
    }
    file.close();
    result=0;
    count=0;
    do {
      value=step(board,size);
      if (count<100) {
        result+=value;
      }
      count++;
    } while(!checkBoard(board,size));
    printf("Total flashes in 100 iterations: %d\n",result);
    printf("Min iterations before all flash at once: %d\n",count);

  } else {
    cout<<"Failed to open file";
  }
}

int step(int **board, int size) {
  int count=0;
  bool checkNewFlashes=true;
  for (int i=0; i<size; i++) {
    for (int j=0; j<size; j++) {
      board[i][j]++;
    }
  }
  while (checkNewFlashes) {
    checkNewFlashes=false;
    for (int i=0; i<size; i++) {
      for (int j=0; j<size; j++) {
        if (board[i][j]>9) {
          count++;
          flash(board,size,i,j);
          checkNewFlashes=true;
        }
      }
    }
  }
  for (int i=0; i<size; i++) {
      for (int j=0; j<size; j++) {
          if (board[i][j]<0) {
            board[i][j]=0;
          }
      }
  }
  return count;
}
void flash(int **board, int size, int row, int column) {
  for (int i=max(0,row-1); i<min(size,row+2); i++) {
    for (int j=max(0,column-1); j<min(size,column+2); j++) {
      board[i][j]++;
    }
  }
  board[row][column]=-10;
}
bool checkBoard(int **board, int size) {
  for (int i=0; i<size; i++) {
    for (int j=0; j<size; j++) {
      if (board[i][j]!=0) {
        return false;
      }
    }
  }
  return true;
}
