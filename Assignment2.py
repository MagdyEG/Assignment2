#Find the missing "letter"

import string
def find_missing_letter(chars):
    for i in string.ascii_lowercase:
        if i not in chars:
            return i[0]






print(find_missing_letter(list(input("enter letters:")) ))
           




#Find the missing "number"

def missing_no(nums):
    

    for i in range(min(nums), max(nums) + 1):
        if i not in nums :
            return i



nums = [1,2,4,5,6]
print(missing_no(nums))

