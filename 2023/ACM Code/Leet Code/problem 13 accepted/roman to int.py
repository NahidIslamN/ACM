class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        result = 0
        prev_value = 0

        for char in s:
            value = roman_values[char]
            if value > prev_value:
                # If the current value is greater than the previous value,
                # it means subtraction is required.
                result += value - 2 * prev_value
            else:
                result += value
            prev_value = value

        return result

# Test the function
solution = Solution()
roman_numeral = "MCMXCIV"
print("Integer representation:", solution.romanToInt(roman_numeral))

        
