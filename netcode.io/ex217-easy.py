

def containsDuplicate(nums):
    """
       Function receive a list and return True if have numbers
       duplicate, and return false if have not.
    """
    
    number_accounts = {}

    for num in nums:
        if num in number_accounts:
            number_accounts[num] += 1
        else:
            number_accounts[num] = 1
    
    for num in number_accounts:
        if number_accounts[num] > 1:
            return True
    return False
   

nums = [1, 2, 3, 4, 4]
print(containsDuplicate(nums))