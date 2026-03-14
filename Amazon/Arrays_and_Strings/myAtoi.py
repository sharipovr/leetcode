class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        INT_MAX = 2**31 - 1     # Max 32-bit int value
        INT_MIN = -2**31        # Min 32-bit int value

        i = 0       # Start index
        n = len(s)  # Length of the string

        # Skip leading whitespaces
        while i < n and s[i] == ' ':
            i += 1  # Move index past space

        # Handle empty or all-whitespace strings
        if i == n:
            return 0    # Ni number exists

        # Handle sign if present
        sign = 1    # Default is positive
        if i < n and s[i] == '+':
            i += 1  # skip the plus
        elif i < n and s[i] == '-':
            sign = -1   # Mark as negative
            i += 1

        result = 0  # This will store our final number

        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')    # Convert char to number

            # Check for overflow before adding the digit!
            if result > (INT_MAX - digit) // 10:
                # If overflow, clamp to bounds
                return INT_MAX if sign == 1 else INT_MIN
            
            result = result * 10 + digit    # shift left and add digit
            i += 1  # Move to the next char
        
        result *= sign  # Apply sign

        return result