#include <vector>

using namespace std;

#define MAX_VALUE 100
class Profitable_Scheme_Solution {
public:
	int profitableSchemes(int G, int P, vector<int>& group, vector<int>& profit)
	{
		int MOD = 1e9 + 7;
		int S[MAX_VALUE][MAX_VALUE + 1][MAX_VALUE + 1];
		int size = group.size();
		memset(S, 0, sizeof(S));
		if (G <= 0) return 0;
		// S(k,G,P) = S(k-1, G, P) + S(k-1, G-group(k), P - profit(k))
		for (int i = 0; i <= MAX_VALUE; i++)
		{
			for (int j = 0; j <= MAX_VALUE; j++)
			{
				if ((group[0] <= i) && (profit[0] >= j))
					S[0][i][j] = 1;
				else
					S[0][i][j] = 0;
			}
		}
		for (int k = 1; k<size; k++)
		{
			for (int i = 0; i <= MAX_VALUE; i++)
			{
				for (int j = 0; j <= MAX_VALUE; j++)
				{
					if (i - group[k] < 0)
						S[k][i][j] = S[k - 1][i][j];
					else if (j - profit[k] <= 0)
						S[k][i][j] = S[k - 1][i][j] + S[k - 1][i - group[k]][0] + 1;
					else
						S[k][i][j] = S[k - 1][i][j] + S[k - 1][i - group[k]][j - profit[k]];
					S[k][i][j] = S[k][i][j] % MOD;
				}
			}
		}
		//
		return S[size - 1][G][P] % MOD;
	}
};