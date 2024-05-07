"""
Problem:

Given a list of numbers, return whether any two sums to k. For example, given
[10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

def day1(nums: list, k: int) -> bool:
    s = set(nums)
    for num in s:
        if k - num in s:
            return True
    
    return False
    


if __name__ == '__main__':
    x = [10, 15, 3, 7]
    k = 17
    print(day1(x, k)) # True
