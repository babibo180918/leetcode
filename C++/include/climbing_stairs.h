#include <vector>

class Climbing_Stair_Solution
{
public:
	int climbStairs(int n)
	{
		int s1 = 1, s2 = 0, s;
		if(n<3)
			return n;
		for(int i=2; i<n; i++)
		{
			s = s1 + s2;
			s2 = s1;
			s1 = s;
		}
		return 2*s1+s2;
	}
}

