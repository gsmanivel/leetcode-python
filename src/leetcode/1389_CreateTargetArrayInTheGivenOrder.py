def finalVal():
    nums = [1, 2, 3, 4, 0]
    index = [0, 1, 2, 3, 0]
    result = []
    for i in range(len(nums)):
        result.insert(index[i], nums[i])
    return result


if __name__ == '__main__':
    print(finalVal())

# https://leetcode.com/problems/create-target-array-in-the-given-order/
