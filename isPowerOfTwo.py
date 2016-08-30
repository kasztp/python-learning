class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        if (n <= 0):
            return False
        elif (n == 1):
            return True
        elif ( n % 2 == 0 ):
            n = float(n)
            while ( n >= 2 ):
                    n /= 2
            if (n == 1.0):
                return True
            else:
                return False
        else:
            return False

