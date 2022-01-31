def finalVal():
    nums = [1, 3]
    k = 3
    result = 0
    for i in nums:
        for j in range(len(nums)):
            if i > nums[j] and (i - nums[j]) == k:
                result += 1
    return result


if __name__ == '__main__':
    print(finalVal())

# https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/
