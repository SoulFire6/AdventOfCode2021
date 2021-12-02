#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
  ifstream file;
  string command;
  int amount;
  int horizontal=0,vertical=0;
  int result;
  file.open("in.txt");
  if (file.is_open()) {
    while(!file.eof()) {
      getline(file,command,' ');
      file>>amount;
      if (command.find("forward")!=-1) {
        cout<<"\nGoing forward "<<amount;
        horizontal+=amount;
      } else if (command.find("down")!=-1) {
        cout<<"\nGoing down "<<amount;
        vertical+=amount;
      } else if (command.find("up")!=-1) {
        cout<<"\nGoing up "<<amount;
        vertical-=amount;
      } else {
        cout<<"Error";
      }
    }
  file.close();
  result=horizontal*vertical;
  cout<<"\n\nTotal "<<result;
  } else {
    cout<<"Failed to open file";
  }
}
