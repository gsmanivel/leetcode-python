def coding():
    namelist = ['mani', 'sin2', 'ayush']
    nums = [5, 3, 1, 10]
    print(namelist)

    # Create empty list
    print(list())

    # reverse
    nums.reverse()
    print('nums List after reverse:', nums)

    # find first index of an element
    indexOfsin2 = namelist.index('sin2')
    print('indexOfsin2--', indexOfsin2)

    # Clear
    namelist.clear()
    print('namelist after clearing--', namelist)

    nums.insert(3, 9)
    print(nums)

    nums.pop(1)
    print(nums)


if __name__ == '__main__':
    coding()
