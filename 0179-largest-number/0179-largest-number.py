from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums):
        # Convert numbers to strings
        nums_str = list(map(str, nums))
        
        # Custom comparator: compare which concatenation is larger
        def compare(x, y):
            if x + y > y + x:
                return -1  # x should come before y
            elif x + y < y + x:
                return 1   # y should come before x
            else:
                return 0
        
        # Sort using the custom comparator
        nums_str.sort(key=cmp_to_key(compare))
        
        # Join the numbers
        result = ''.join(nums_str)
        
        # Handle case with leading zeros
        return '0' if result[0] == '0' else result

        