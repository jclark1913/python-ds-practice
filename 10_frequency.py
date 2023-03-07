def frequency(lst:list, search_term):
    """Return frequency of term in lst.

        >>> frequency([1, 4, 3, 4, 4], 4)
        3

        >>> frequency([1, 4, 3], 7)
        0
    """
    nums = [1, 2, 3]
    print(nums.count(1))
    return lst.count(search_term)