class Solution(object):
    def isPossibleDivide(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        size = len(nums)
        cols = size // k
        if cols * k != size:
            return False
        nums.sort()
        l = []
        for i in range(k):
            l.append([])
        for num in nums:
            l[(num + 1) % k].append(num)
        try:
            for i in range(cols):
                switch = False
                for j in range(k - 1):
                    if not switch and l[j][i] - l[j+1][i] == k - 1:
                        switch = True
                    elif l[j+1][i] - l[j][i] != 1:
                        return False
        except:
            return False
        return True


sol = Solution()
result = sol.isPossibleDivide([1,2,3,3,4,4,5,6], 4)
print(result == True)

result = sol.isPossibleDivide([1,2,3,3,4,4,5,6], 5)
print(result == False)

result = sol.isPossibleDivide([1,2,3,3,4,4,5,6], 2)
print(result == True)

result = sol.isPossibleDivide([3,2,1,2,3,4,3,4,5,9,10,11], 3)
print(result == True)

result = sol.isPossibleDivide([3,2,1,2,3,4,3,4,5,9,10,11], 6)
print(result == False)

result = sol.isPossibleDivide([3,3,2,2,1,1], 3)
print(result == True)

result = sol.isPossibleDivide([1,2,3,4], 3)
print(result == False)

result = sol.isPossibleDivide([1], 1)
print(result == True)

result = sol.isPossibleDivide([1], 2)
print(result == False)

result = sol.isPossibleDivide([1, 2], 1)
print(result == True)

result = sol.isPossibleDivide([1, 2, 3], 2)
print(result == False)
