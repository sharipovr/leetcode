class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # if the input list is empty or has only one element, return 0
        if not height or len(height) < 2:
            return 0

        left = 0 # Start pointer at the leftmost line
        right = len(height) - 1 # Start pointer at the rightmost line

        max_area = 0    # Store the maximum area found

        # Loop until the two pointers meet
        while left < right:
            # Calculate width betwwen left and right pointers
            width = right - left
            # Find the minimum height between left and right
            curr_height = min(height[left], height[right])
            # Calculate area of container formed by lines left and right
            area = width * curr_height
            # Update max_area if this area is bigger than current max_area
            if area > max_area:
                max_area = area

            # Move the pointer pointing to the shorter line inward
            if height[left] < height[right]:
                left += 1   # move left pointer right
            else:
                right -= 1  # move right pointer left

        # Return the largest area discovered
        return max_area


