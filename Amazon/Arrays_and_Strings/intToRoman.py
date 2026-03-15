def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman_numerals = [
            (1000, "M"),        # 1000 maps to M
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]

        # Start with an empty result string
        result = ""
        # Loop over each value and symbol in the mapping
        for value, symbol in roman_numerals:
            # While the current number is greater than or equal to this value
            while num >=  value:
                result += symbol
                num -= value

        # Return the Roman numerla string we build
        return result