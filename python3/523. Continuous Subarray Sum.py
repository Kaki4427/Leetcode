def checkSubarraySum(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    # method 1 failed
    l = len(nums)

    if l == 1:
        return False

    if l == 2:
        if sum(nums)%k==0:
            return True
        else:
            return False

    for d in range(2,l+1):
        for i in range(l-d+1):
            if i+d <= l:
                if sum(nums[i:i+d])%k ==0:
                    return True
    return False

    # solution: Hash map approach 40/40
    # initialize the hash map with index 0 for sum 0
    hash_map = {0: 0}
    s = 0
    for i in range(len(nums)):
        s += nums[i]
        # if the remainder s % k occurs for the first time
        if s % k not in hash_map:
            hash_map[s % k] = i + 1
        # if the subarray size is at least two
        elif hash_map[s % k] < i:
            return True
    return False
