# LeetCode 1365: How Many Numbers Are Smaller Than the Current Number
# Difficulty: Easy
# Topics: Arrays, Hash Table, Sorting, Counting sort
# Language: Python 3

from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        
        for i in nums:
            count = 0
            n = i
            for x in nums:
                if x < n:
                    count += 1
            res.append(count)

        return res