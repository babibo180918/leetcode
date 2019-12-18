#include <iostream>
#include "3sum.h"
#include "rotate_list.h"

int main()
{
	// 3sum test
	//vector<int> testcase{-1,0,1,2,-1,-4,0,-3,0,3};
	//Solution_3sum solution;
	//vector<vector<int>> output = solution.threeSum(testcase);
	//cout<<"Output:" <<endl;
	//for(vector<vector<int>>::iterator it = output.begin(); it!=output.end(); ++it)
	//{
	//	cout<<"[" <<(*it)[0] <<" " <<(*it)[1] <<" " <<(*it)[2] <<"]" <<endl;
	//}

	// rotate list test
	ListNode *list = new ListNode(0);
	ListNode *tail = list;
	cout << "input: [" << tail->val;
	for (int i = 1; i < 10; i++)
	{
		ListNode *node = new ListNode(i);
		tail->next = node;
		tail = node;
		cout << " " <<tail->val;
	}
	cout << "]" << endl;

	Solution_rotate_list rotate_list;
	list = rotate_list.rotateRight(list, 4);
	tail = list;
	cout << "output: [";
	while (tail != NULL)
	{
		cout << " " <<tail->val;
		tail = tail->next;
	}
	cout << "]" << endl;

	//
	return 0;
}
