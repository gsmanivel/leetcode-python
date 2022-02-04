def finalVal():
    nums = [5, 6, 2, 7, 4]
    mini = 0
    maxi = 0
    # for i in range(0, len(nums)):
    #     for j in range(i+1, len(nums)):
    #         multiply = nums[i] * nums[j]
    #
    #         if multiply > maxi:
    #             maxi = multiply
    #
    #         if i == 0 and j == 1:
    #             mini = maxi
    #
    #         if multiply < mini:
    #             mini = multiply

    nums.sort()
    return (nums[len(nums)-1] * nums[len(nums)-2]) - (nums[0] * nums[1])


if __name__ == '__main__':
    print(finalVal())

    # https://leetcode.com/problems/maximum-product-difference-between-two-pairs/
