class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Create an empty dictionary to store numbers and their indicies
        num_to_index = {}
        # Loop through each index and value in nums
        for i, num in enumerate(nums):
            # Calculate the complenebt needed to reach the target
            complement = target - num
            # Check if the complement is already in the dictionary
            if complement in num_to_index:
                # If found, return the indicies fo complement and current number
                return [num_to_index[complement], i]
            # Otherwise, add the current number and its index to the dictionary
            num_to_index[num] = i
        # Should never reach here sinse exactly one solution exists
        return []
    

