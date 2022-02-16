def finalVal():
    accounts = [[1,5],[7,3],[3,5]]
    
    val= 0
    for account in accounts:
        sum=0
        for num in account:
            sum = sum + num
        val = max(val,sum)
    return val


if __name__ == '__main__':
    print(finalVal())
    
    
    #https://leetcode.com/problems/richest-customer-wealth/