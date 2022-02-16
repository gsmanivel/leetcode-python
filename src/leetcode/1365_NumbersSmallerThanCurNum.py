def finalVal():
    nums = [8, 1, 2, 2, 3]
    rest = [0] * len(nums)
    for i in range(len(nums)):
        curNum = nums[i]
        maxCount = 0
        for j in range(len(nums)):
            if curNum > nums[j]:
                maxCount = maxCount + 1
        rest[i] = maxCount
    return rest


if __name__ == '__main__':
    print(finalVal())

# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
