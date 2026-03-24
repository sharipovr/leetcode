class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # Sort  the array to make duplicate handling and two-pointer search easier
        nums.sort()
        n = len(nums)
        result = []  # initialize and empty array to store triplets

        # Loop through each element, up to the third-to-last
        for i in range(n - 2):
            # Skip duplicate elements for i to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # skip this iterations if current element is same as previous

            left, right = i + 1, n - 1  # set left and right pointers

            # Use two pointers to find pairs that sum to nums[i]
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    # Found a triplet, add to result
                    result.append(
                        [nums[i], nums[left], nums[right]]
                    )  # add triplet to result

                    # Move left and right pointers
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1  # skip duplicate left values
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1  # skip duplicate right values

                    left += 1  # move left pointer forward
                    right -= 1  # move right pointer backward

                elif total < 0:
                    left += 1  # sum is too small, move left pointer forward
                else:
                    right -= 1  # sum is too large, move right pointer backward

        return result
