using namespace std;

 //Definition for singly-linked list.
 struct ListNode {
     int val;
     ListNode *next;
     ListNode(int x) : val(x), next(NULL) {}
};

class Solution_rotate_list {
public:
	ListNode* rotateRight(ListNode* head, int k)
	{
		if (head == NULL)
			return head;
		ListNode *node = head, *new_tail = NULL, *tail = NULL;
		int len = lengthOfSLL(head, &tail);
		k = k%len;
		for (int i = 0; i<len - k - 1; i++)
		{
			node = node->next;
		}
		new_tail = node;
		node = node->next;
		if (node != NULL)
		{
			new_tail->next = NULL;
			tail->next = head;
			head = node;
		}
		return head;
	}
private:
	int lengthOfSLL(ListNode *head, ListNode **pTail)
	{
		int len = 0;
		ListNode *node = head;
		*pTail = head;
		while (node != NULL)
		{
			len++;
			*pTail = node;
			node = node->next;
		}
		return len;
	}
};
