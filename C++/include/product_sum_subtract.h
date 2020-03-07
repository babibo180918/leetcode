
class Product_Sum_Subtract_Solution
{
public:
	int P(int n)
	{
		int p=1;
		while(n!=0)
		{
			p *= n%10;
			n /= 10;
		}
		return p;
	}

	int S(int n)
	{
		int s = 0;
		while (n!=0)
		{
			s += n%10;
			n /= 10;
		}
		return s;
	}

	int subtractProductAndSum(int n)
	{
		int p = 1;
		int s = 0;
		int digit;
		while (n!=0)
		{
			digit = n%10;
			p *= digit;
			s += digit;
			n /= 10;
		}
		return p-s;
	}
}
