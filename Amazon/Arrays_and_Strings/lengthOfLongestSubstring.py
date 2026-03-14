class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Dictionary to store the last index of each character
        last_seen = {}  # Keeps track of where each character was last seen
        # Start of the current window
        start = 0       # This is the left boundary of our window
        # Maximum length found so far
        max_length = 0  # Will store the answer

        # Loop through each character in the string
        for end in range(len(s)):
            char = s[end]   # current character we are lopking at
            # If we have seen this character before and it's inside our current windows
            if char in last_seen and last_seen[char] >= start:
                # Move start to the right of the previous occurrence
                start = last_seen[char] + 1 # Jump past the repeated character

            # Update the last seen indx for the character
            last_seen[char] = end   # Remember where we saw this character
            # Update max_length if this windows is longer than previous best
            max_length = max(max_length, end - start + 1)   # calculate window

        # Return the largest length found
        return max_length




