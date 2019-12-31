# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret = NodeList(0)
        val = 0
        last = ret
        while True:
            if l1 is not None:
                val += l1.val
                l1 = l1.next
            if l2 is not None:
                val += l2.val
                l2 = l2.next
            if ret is None:
                ret = ListNode(val)
                last = ret
            else:
                last.next = ListNode(val)
                last = last.next
            if l1 is None and l2 is None and val == 0:
                break
        if ret is None:
            ret = ListNode(0)
        return ret

            
def printList(head):
    while head is not None:
        print(head.val, end=' ')
        head = head.next
    print()


def makeList(l):
    if len(l) == 0:
        return None
    head = ListNode(l[0])
    cur = head
    for a in l[1:]:
        cur.next = ListNode(a)
        cur = cur.next
    return head

sol = Solution()

one=makeList([1,2,3])
two=makeList([4,5,6])
expect=makeList([5,7,9])
result=sol.addTwoNumbers(one, two)
print('Expect:')
printList(expect)
print('Result:')
printList(result)


one=makeList([7,2,1])
two=makeList([4,5,6])
expect=makeList([1,8,7])
result=sol.addTwoNumbers(one, two)
print('Expect:')
printList(expect)
print('Result:')
printList(result)

one=makeList([2,2,9])
two=makeList([4,5,6])
expect=makeList([6,7,5,1])
result=sol.addTwoNumbers(one, two)
print('Expect:')
printList(expect)
print('Result:')
printList(result)

one=makeList([0])
two=makeList([0])
expect=makeList([0])
result=sol.addTwoNumbers(one, two)
print('Expect:')
printList(expect)
print('Result:')
printList(result)

one=makeList([1, 3, 4])
two=makeList([5, 2])
expect=makeList([6, 5, 4])
result=sol.addTwoNumbers(one, two)
print('Expect:')
printList(expect)
print('Result:')
printList(result)

two=makeList([5, 2])
one=makeList([1, 3, 4])
expect=makeList([6, 5, 4])
result=sol.addTwoNumbers(one, two)
print('Expect:')
printList(expect)
print('Result:')
printList(result)

two=makeList([5, 9])
one=makeList([1, 3, 4])
expect=makeList([6, 2, 5])
result=sol.addTwoNumbers(one, two)
print('Expect:')
printList(expect)
print('Result:')
printList(result)

two=makeList([2, 3, 0, 1])
one=makeList([1, 3, 0, 4])
expect=makeList([3, 6, 0, 5])
result=sol.addTwoNumbers(one, two)
print('Expect:')
printList(expect)
print('Result:')
printList(result)
