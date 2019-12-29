#include <map>
#include <vector>

using namespace std;

class Solution_array_to_k_subset
{
public:
	bool isPossibleDivide(vector<int> nums, int k)
	{
		map<int, int> hist;
		for(int i=0; i<nums.size(); i++)
		{
			hist[nums[i]]++;
		}
		while(hist.size() > 0)
		{
			int val = hist.begin()->first;
			for(int i=val; i<val+k; i++)
			{
				if(hist.find(i) == hist.end())
					return false;
				hist[i]--;
				if(hist[i] == 0)
					hist.erase(i);
			}
		}
		return true;
	}
};
