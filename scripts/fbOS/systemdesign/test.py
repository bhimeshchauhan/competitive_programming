def subarraySum(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    if not nums:
        return 0
    tally = {0:1}
    n = len(nums)
    count = 0
    s = 0
    for num in nums:
        s += num
        if s - k in tally:
            count += tally[s-k]
        if s in tally:
            tally[s] += 1
        else:
            tally[s] = 1
    return count
    