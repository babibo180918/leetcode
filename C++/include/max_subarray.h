#include <vector>

class Solution_max_subarray
{
public:
	int maxSubArray(vector<int> &nums)
	{
		int max = nums[0];
		int sum = nums[0];
		for(int i=1; i<nums.size(); i++)
		{
			if(sum < 0)
				sum = nums[i];
			else
				sum += nums[i];
			if(sum>max)
				max = sum;
		}
		return max;
	}	
}
