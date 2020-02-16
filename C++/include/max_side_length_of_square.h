#include <vector>

class Max_Side_Length_of_Square_Solution
{
public:
	int maxSideLength(vector<vector<int>> &mat, int threshold)
	{
		int r = mat.size();
        int c = mat[0].size();
        int arr[r+10][c+10];
        int ans=0,val;
        memset(arr,0,sizeof(arr));
        for(int i=0;i<c;i++)
            for(int j=1;j<r;j++)
                mat[j][i]+=mat[j-1][i];
        for(int i=0;i<r;i++)
            for(int j=1;j<c;j++)
                mat[i][j]+=mat[i][j-1];
        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                arr[i+1][j+1] = mat[i][j];
            }
        }
        for(int l=0;l<min(r,c);l++){
            for(int i=r;i>l;i--){
                for(int j=c;j>l;j--){
                    val = arr[i][j]-(arr[i-(l+1)][j]+arr[i][j-(l+1)])+arr[i-(l+1)][j-(l+1)];
                    if(val<=threshold){
                        ans=max(ans,l+1);
                    }
                }
            }
        }
		return ans;
	}
}
