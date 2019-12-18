
// Definition for singly-linked list.
 struct ListNode {
     int val;
     ListNode *next;
     ListNode(int x) : val(x), next(NULL) {}
 };

class Solution {
public:
	ListNode* addTwoNumbers(ListNode* l1, ListNode* l2)
	{
		ListNode *sum = NULL, *node = NULL;
		int rem = l1->val + l2->val;
		int digit = rem % 10;
		rem = rem / 10;
		node = new ListNode(digit);
		sum = node;
		l1 = l1->next;
		l2 = l2->next;
		while (1)
		{
			if ((l1 == NULL) && (l2 == NULL))
			{
				if (rem > 0)
					node->next = new ListNode(rem);
				break;
			}
			if (l1 != NULL)
			{
				rem += l1->val;
				l1 = l1->next;
			}
			if (l2 != NULL)
			{
				rem += l2->val;
				l2 = l2->next;
			}
			digit = rem % 10;
			rem = rem / 10;
			node->next = new ListNode(digit);
			node = node->next;
		}
		return sum;
	}
};