def finalVal():
    nums = [2,5,1,3,4,7]
    n = 3
    
    rest = [0]* len(nums)
    i = 0
    j = 0
    for i in range(len(nums)/2):
        rest[j] = nums[i]
        rest[j+1] = nums[i+n]
        j = j +2
    return rest
    

if __name__ == '__main__':
    print(finalVal())
    
    
    #https://leetcode.com/problems/shuffle-the-array/