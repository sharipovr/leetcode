def romanToInt(self, s):
    """
    :type s: str
    :rtype: int
    """
    # Map Roman numerals to integer values
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    total = 0  # Initialize result
    i = 0  # Start index for string iteration

    while i < len(s):  # Iterate while we have characters remaining
        # Check if this is a subtractive case (not last char and current < next)
        if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
            total -= roman[s[i]]  # Subtract current if followed by bigger value
        else:
            total += roman[s[i]]  # Otherwise, add the value
        i += 1  # Move to the next character

    return total
