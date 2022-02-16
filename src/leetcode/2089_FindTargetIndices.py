def finalVal():
    nums = [1, 2, 5, 2, 3]
    target = 2

    result = []
    nums.sort()
    for i in range(len(nums)):
        if nums[i] == target:
            result.append(i)
    return result


if __name__ == '__main__':
    print(finalVal())

    # https://leetcode.com/problems/find-target-indices-after-sorting-array/
