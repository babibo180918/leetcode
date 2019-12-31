class Solution(object):
    def maxSubArray(self, nums):
        max_val=nums[0]
        cur_val=nums[0]
        for a in nums[1:]:
            if cur_val <= 0:
                cur_val = a
            else:
                cur_val += a
            max_val = max(cur_val, max_val)
        return max_val

sol = Solution()

output=sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print('Result : %', output)
print('Expect : %', 6)

output=sol.maxSubArray([-3,-2,-1,-4])
print('Result : %', output)
print('Expect : %', -1)

output=sol.maxSubArray([3,2,1,4])
print('Result : %', output)
print('Expect : %', 10)

output=sol.maxSubArray([])
print('Result : %', output)
print('Expect : %', 10)

