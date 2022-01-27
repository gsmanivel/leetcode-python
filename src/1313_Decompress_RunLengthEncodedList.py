def finalVal():
    nums = [1, 1, 2, 3]

    result = []
    for i in range(0, len(nums), 2):
        result.extend([nums[i + 1]] * nums[i])

    return result


if __name__ == '__main__':
    print(finalVal())

#  https://leetcode.com/problems/decompress-run-length-encoded-list/
