#include <iostream>
#include "3sum.h"


int main()
{
	vector<int> testcase{-1,0,1,2,-1,-4,0,-3,0,3};
	Solution_3sum solution;
	vector<vector<int>> output = solution.threeSum(testcase);
	cout<<"Output:" <<endl;
	for(vector<vector<int>>::iterator it = output.begin(); it!=output.end(); ++it)
	{
		cout<<"[" <<(*it)[0] <<" " <<(*it)[1] <<" " <<(*it)[2] <<"]" <<endl;
	}
	return 0;
}
