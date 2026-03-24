class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()  # sort array for two-pointer technique
        n = len(nums)

        closest_sum: int = (
            nums[0] + nums[1] + nums[2]
        )  # initialize closest to first triplet sum

        # Loop through each index
        for i in range(n - 2):  # Only go up to n-3, since we need 3 elements
            left = i + 1  # Set the left pointer just after i
            right = n - 1  # Set the right pointer at the end

            while left < right:  # While pointers don't cross
                curr_sum = nums[i] + nums[left] + nums[right]  # calculate current sum

                # If this sum is closer to target then previous closest, update
                if abs(curr_sum - target) < abs(closest_sum - target):
                    closest_sum = curr_sum  # Update closest sum

                # If exact match, return immediatly
                if curr_sum == target:
                    return curr_sum  # Found the best possible sum

                # Move pointers based on comparison
                if curr_sum < target:
                    left += 1  # Increase sum by moving left pointer right
                else:
                    right -= 1  # Decrease sum by moving right poinetr left

        return closest_sum
