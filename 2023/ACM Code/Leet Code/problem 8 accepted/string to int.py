class Solution:
    def myAtoi(self, s: str) -> int:

        # Remove leading whitespace
        s = s.lstrip()

        # Check if the string is empty after stripping whitespace
        if not s:
            return 0

        # Initialize variables
        sign = 1
        result = 0
        i = 0

        # Check for sign
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1

        # Parse digits
        while i < len(s) and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1

        # Apply sign
        result *= sign

        # Clamp result to the range [-2^31, 2^31 - 1]
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        if result > INT_MAX:
            return INT_MAX
        elif result < INT_MIN:
            return INT_MIN
        else:
            return result

# Test the function

x = Solution()
print(x.myAtoi("4193           with words"))

