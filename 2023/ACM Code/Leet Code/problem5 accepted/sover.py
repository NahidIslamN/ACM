class Solution:
    def longestPalindrome(self, user_str : str) -> str:
        lenght = len(user_str)        
        final_substr = ""
        demo_str = ""
        pointer1 = 0
        pointer2 = 1
        if lenght <= 1000:
            while True:
                if pointer1< lenght:
                
                    if user_str[pointer1: pointer2] == user_str[pointer1: pointer2][ ::-1]:
                        demo_str = user_str[pointer1: pointer2]
                      
                        if len(demo_str) >len(final_substr):
                            final_substr = demo_str
                            if pointer2 < lenght :
                                pointer2 = pointer2+1
                            else:
                                pointer1 = pointer1+1
                                pointer2 = pointer1 + 1
                        else:
                            if pointer2 < lenght :
                                pointer2 = pointer2+1
                            else:
                                pointer1 = pointer1+1
                                pointer2 = pointer1 + 1
                        
                    else:
                        if pointer2 < lenght :
                            pointer2 = pointer2+1
                        else:
                            pointer1 = pointer1+1
                            pointer2 = pointer1 + 1
                else:
                    break
            return final_substr
        



        
x = Solution()
print(x.longestPalindrome(user_str="abab")  )                      
                            
                            






        
