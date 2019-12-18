#include <vector>
#include <algorithm>
#include <cstdlib>
#include <map>

using namespace std;

class Solution1_3sum {
public:

	int isDuplicate(vector<int> nplet1, vector<int> nplet2)
	{
		if ((nplet1[0] * nplet1[1] * nplet1[2] == nplet2[0] * nplet2[1] * nplet2[2]) &&
			(nplet1[0] * nplet1[1] + nplet1[1] * nplet1[2] + nplet1[0] * nplet1[2] == nplet2[0] * nplet2[1] + nplet2[1] * nplet2[2] + nplet2[0] * nplet2[2])
			)
			return 1;
		else
			return 0;
	}

	void sort(vector<int>& nums)
	{
		for (int i = 0; i < nums.size(); i++)
		{
			for (int j = 0; j < nums.size() - i - 1; j++)
			{
				if (nums[j] > nums[j + 1])
				{
					int tmp = nums[j];
					nums[j] = nums[j + 1];
					nums[j + 1] = tmp;
				}
			}
		}
	}

	vector<vector<int>> threeSum(vector<int>& nums)
	{
		vector<vector<int>> out;
		sort(nums);
		for (int i = 0; i < nums.size() - 1; i++)
			for (int j = i + 1; j < nums.size(); j++)
				for (int k = j + 1; k < nums.size(); k++)
				{
					if (((nums[i] + nums[j] + nums[k]) == 0))
					{
						vector<int> triplet{ nums[i], nums[j], nums[k] };
						out.push_back(triplet);
					}
					else if (((nums[i] + nums[j] + nums[k]) > 0))
						i = j = k = nums.size();
				}
		//
		for (int i = out.size() - 1; i >= 1; i--)
		{
			for (int j = i - 1; j >= 0; j--)
			{
				if (isDuplicate(out[j], out[i]))
				{
					out.erase(out.begin() + j);
					i--;
				}
			}
		}

		return out;
	}
};

class Solution2_3sum {
public:
	int isDuplicate(vector<int> nplet1, vector<int> nplet2)
	{
		if ((nplet1[0] * nplet1[1] * nplet1[2] == nplet2[0] * nplet2[1] * nplet2[2]) &&
			(nplet1[0] * nplet1[1] + nplet1[1] * nplet1[2] + nplet1[0] * nplet1[2] == nplet2[0] * nplet2[1] + nplet2[1] * nplet2[2] + nplet2[0] * nplet2[2])
			)
			return 1;
		else
			return 0;
	}

	void sort(vector<int>& nums)
	{
		for (int i = 0; i < nums.size(); i++)
		{
			for (int j = 0; j < nums.size() - i - 1; j++)
			{
				if (nums[j] > nums[j + 1])
				{
					int tmp = nums[j];
					nums[j] = nums[j + 1];
					nums[j + 1] = tmp;
				}
			}
		}
	}

	vector<vector<int>> threeSum(vector<int>& nums)
	{
		vector<vector<int>> out;
		sort(nums);
		int max_i = nums.size() - 2;
		int max_j = nums.size() - 1;
		int max_k = nums.size();
		for (int i = 0; i < max_i; i++)
		{
			if (3 * nums[i] > 0)
				break;
			for (int j = i + 1; j < max_j; j++)
			{
				if ((nums[i] + 2 * nums[j]) > 0)
					break;
				for (int k = j + 1; k < max_k; k++)
				{
					if (((nums[i] + nums[j] + nums[k]) == 0))
					{
						vector<int> triplet{ nums[i], nums[j], nums[k] };
						out.push_back(triplet);
					}
					else if (((nums[i] + nums[j] + nums[k]) > 0))
					{
						break;
					}
				}
			}
		}
		//
		for (int i = out.size() - 1; i >= 1; i--)
		{
			for (int j = i - 1; j >= 0; j--)
			{
				if (isDuplicate(out[j], out[i]))
				{
					out.erase(out.begin() + j);
					i--;
				}
			}
		}

		return out;
	}
};

class Solution3_3sum {
public:
	void sort(vector<int>& nums)
	{
		for (int i = 0; i < nums.size(); i++)
		{
			for (int j = 0; j < nums.size() - i - 1; j++)
			{
				if (nums[j] > nums[j + 1])
				{
					int tmp = nums[j];
					nums[j] = nums[j + 1];
					nums[j + 1] = tmp;
				}
			}
		}
	}

	vector<vector<int>> threeSum(vector<int>& nums)
	{
		vector<vector<int>> out;
		sort(nums);
		//

		for (int i = 0; i < nums.size(); i++)
		{
			printf("%d, ", nums[i]);
			if (!(i % 100))
				printf("\n");
		}
		//
		int center = -1;
		for (int i = 0; i < nums.size(); i++)
		{
			if (nums[i] >= 0)
			{
				center = i;
				break;
			}
		}
		//
		for (int i = 0; i <= center; i++)
		{
			if ((i > 0) && (nums[i] == nums[i - 1]))
				continue;
			for (int j = nums.size() - 1; j >= center; j--)
			{
				if ((j < nums.size() - 1) && (nums[j] == nums[j + 1]))
					continue;
				if (nums[i] + nums[j] > 0)
				{
					for (int k = i + 1; k < center; k++)
					{
						if ((k > i + 1) && (nums[k] == nums[k - 1]))
							continue;
						if ((nums[i] + nums[j] + nums[k]) == 0)
						{
							vector<int> triplet{ nums[i], nums[k], nums[j] };
							out.push_back(triplet);
						}
						else if (((nums[i] + nums[j] + nums[k]) > 0))
							break;
					}
				}
				else if (nums[i] + nums[j] < 0)
				{
					for (int k = center; k < j; k++)
					{
						if ((k > center) && (nums[k] == nums[k - 1]))
							continue;
						if ((nums[i] + nums[j] + nums[k]) == 0)
						{
							vector<int> triplet{ nums[i], nums[k], nums[j] };
							out.push_back(triplet);
						}
						else if (((nums[i] + nums[j] + nums[k]) > 0))
							break;
					}
				}
				else
				{
					for (int k = i + 1; k < j; k++)
					{
						if ((k > i + 1) && (nums[k] == nums[k - 1]))
							continue;
						if ((nums[i] + nums[j] + nums[k]) == 0)
						{
							vector<int> triplet{ nums[i], nums[k], nums[j] };
							out.push_back(triplet);
						}
						else if (((nums[i] + nums[j] + nums[k]) > 0))
							break;
					}
				}

			}
		}
		return out;
	}
};

/**
 *	Best solution with the complexity O(n^2) *
 */
class Solution_3sum {
public:

	void sort(vector<int>& nums)
	{
		for (int i = 0; i < nums.size(); i++)
		{
			for (int j = 0; j < nums.size() - i - 1; j++)
			{
				if (nums[j] > nums[j + 1])
				{
					int tmp = nums[j];
					nums[j] = nums[j + 1];
					nums[j + 1] = tmp;
				}
			}
		}
	}

	vector<vector<int>> threeSum(vector<int>& nums)
	{
		vector<vector<int>> out;
		//sort(nums.begin(), nums.end());
		sort(nums);
		int center = -1;
		multimap<int, pair<int, int>> hashtable;
		for (int i = 0; i < nums.size(); i++)
		{
			if ((nums[i] >= 0) && center == -1)
			{
				center = i;
			}
			//
			pair<int, int> p(i, nums[i]);
			hashtable.insert({ nums[i], p });
		}
		//
		for (int i = 0; i <= center; i++)
		{
			if ((i > 0) && (nums[i] == nums[i - 1]))
				continue;
			for (int j = nums.size() - 1; j >= center; j--)
			{
				if ((j < nums.size() - 1) && (nums[j] == nums[j + 1]))
					continue;
				pair <multimap<int, pair<int, int>>::iterator, multimap<int, pair<int, int>>::iterator> got = hashtable.equal_range(-(nums[i] + nums[j]));
				for (multimap<int, pair<int, int>>::iterator it = got.first; it != got.second; ++it)
				{
					if ((it->second).first > i && (it->second).first < j)
					{
						vector<int> triplet{ nums[i], (it->second).second, nums[j] };
						out.push_back(triplet);
						break;
					}
				}
			}
		}
		return out;
	}
};
