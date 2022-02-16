def finalVal():
    nums = [3, 4, 5, 6, 7, 8]
    result = 0
    wholeXR = 0
    for i in range(len(nums)):
        result = result + nums[i]
        wholeXR = wholeXR ^ nums[i]
        innerLen = i+1
        print("-----------")
        for j in range(i+1, len(nums)):
            for k in range(i+1, innerLen+1):
                result = result + (nums[i] ^ nums[k])
                if k == innerLen:
                    innerLen += 1
                    break
    return result + wholeXR

    # for i in range(len(nums)):
    #     result = result + nums[i]
    #     wholeXR = wholeXR ^ nums[i]
    #     for j in range(i + 1, len(nums)):
    #         result = result + (nums[i] ^ nums[j])
    #
    # return result + wholeXR


if __name__ == '__main__':
    print(finalVal())

    # https://leetcode.com/problems/sum-of-all-subset-xor-totals/
