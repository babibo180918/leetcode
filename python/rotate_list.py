# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution(object):

    def findLen(self, head):
        result = 0
        return result

    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        """ find list size """
        if head is None:
            return head 
        size = 0
        cur = head
        while cur is not None:
            size += 1
            if cur.next is None:
                if k % size == 0:
                    return head
                else:
                    cur.next = head
                    cur = head
                    break
            cur = cur.next
        move = size - (k % size) 
        for i in range(move - 1):
            cur = cur.next
        head = cur.next
        cur.next = None
        return head

def makeList(l):
    a = None
    for val in l:
        if a is None:
            a = ListNode(val)
            cur = a
        else:
            cur.next = ListNode(val)
            cur = cur.next
    return a

def printList(head):
    while head is not None:
        print(head.val, end=' ')
        head = head.next
    print('')

sol = Solution()

l = [1, 2, 3, 4, 5]
head = makeList(l)
printList(head)
for i in range(6):
    print('rotate -->', i)
    head = makeList(l)
    rotate = sol.rotateRight(head, i)
    printList(rotate)
    print('-----')

l = []
head = makeList(l)
printList(head)
rotate = sol.rotateRight(head, 3)
printList(rotate)


l = [3]
head = makeList(l)
printList(head)
print('rotate -->', 5)
rotate = sol.rotateRight(head, 5)
printList(rotate)
print('-----')


