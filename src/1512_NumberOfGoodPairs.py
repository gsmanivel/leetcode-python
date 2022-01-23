def finalVal():
    nums = [1, 2, 3, 1, 1, 3];

    goodPair = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                goodPair = goodPair + 1
    return goodPair


if __name__ == '__main__':
    print(finalVal())

# https://leetcode.com/problems/number-of-good-pairs/
