def threesum(nums):
    hashtable = {}
    result = []
    no_dup = []
    nums.sort()
    size = len(nums)
    for i in range(size):
        hashtable[nums[i]] = i

    for i in range(size - 1):
        if i > 0 and nums[i] == nums[i - 1]: continue
        for j in range(i + 1, size):
            if j-1 > i and nums[j] == nums[j-1]: continue
            twosum = -(nums[i] + nums[j])
            if twosum in hashtable:
                twosum_index = hashtable[twosum]
                if twosum_index > i and twosum_index > j:
                    result.append([nums[i], nums[j], twosum])
    return result


lists = threesum([-1, 0, 1, 2, -1, -4])
print(lists)
lists = threesum([0,0,0])
print(lists)
