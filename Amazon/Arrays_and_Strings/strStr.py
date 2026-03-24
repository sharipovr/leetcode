class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # if needle is empty, return 0 by convention
        if not needle:
            return 0

        # build LPS (Longest Prefix Suffix) array for needle
        lps = [0] * len(needle) # lps[i] = length of the longest prefix which is also suffix for needle[:i+1]
        length = 0  # length of the previous longest prefix suffix
        i = 1   # lps[0] is always 0, so start from 1

        # Build the LPS array
        while i < len(needle):
            # if current char matches the prefix char 
            if needle[i] == needle[length]:
                length += 1 # Increase the length of the current prefix
                lps[i] = length     # Set lps[i] to the current prefix length
                i += 1  # Move to the next character
            else:
                if length != 0:
                    length = lps[length - 1]   # Try the previous longest

                else:
                    lps[i] = 0  # No prefix found, set to 0
                    i += 1  # Move to the next character
        
        # Now, use the LPS array to search in haystack
        i = 0   # index for haystack
        j = 0   # index for needle

        while i < len(haystack):
            # If characters match, move both pointers
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            # If all characters in needle are matched
            if j == len(needle):
                return i - j # Found the match, return starting index
            elif i < len(haystack) and haystack[i] != needle[j]:
                if j != 0:
                    j = lps[j-1]    # Use LPS to skip ahead in needle
                else:
                    i += 1  # Move to the next character in haystack
        
        # If no match found
        return -1