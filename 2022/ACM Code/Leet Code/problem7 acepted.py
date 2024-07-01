class Solution:
    def reverse(self, x):
        if x.bit_length()>=32:
            return 0
        elif x>0:
            h=str(x)
            result=int(h[::-1])
        else:
            h=str(x)
            h2=h[1:]
            result=int(h[0]+h2[::-1])
        if result.bit_length()>=32:
            return 0
        else:
            return result


    
