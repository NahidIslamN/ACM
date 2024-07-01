class Solution:
    def intToRoman(self, num: int) -> str:
        # Define the Roman numeral symbols and their corresponding values
        roman_numerals = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }

        # Initialize an empty string to store the Roman numeral
        roman_numeral = ''

        # Iterate through the values in descending order
        for value, numeral in roman_numerals.items():
            # Repeat numeral while the value is less than or equal to the input num
            while num >= value:
                roman_numeral += numeral
                num -= value

        return roman_numeral

#test
x = Solution()
print(x.intToRoman(8))
