#include <iostream>
#include<random>
#include<algorithm>
#include<vector>
#include<ctime>
#include<windows.h>
#include<chrono>
#include<cstdlib>
using namespace std;

void rendervisual(vector<int>& data){
	std::cout << "\033[2J\033[H";
		for(int i=0; i<20; i++){
			for(int j=0; j<data[i]; j++){
				cout<<"#";
			}
			cout<<endl;
		}
		//this_thread::sleep_for(chrono::milliseconds(500));
		Sleep(500);
}

int main(){
	vector<int> freqarr, magarr;
	random_device rd;
	mt19937 gen(rd());
	uniform_int_distribution<int> distribution(0,100);
	system("cls");
	do{
		for(int i=0; i<20; i++){
			freqarr.push_back(distribution(gen));//generate random
		}
		auto maxelement=*max_element(freqarr.begin(), freqarr.end());//_/_/ deferencing later only gives iterator
		for(int& i:freqarr){
			i=i*20/(maxelement);
		}
		/*for (int value:freqarr){
			cout<<value<<endl;
		}*/
		rendervisual(freqarr);
		freqarr.clear();

	}while(true);
	system("cls");
	return 0;
}