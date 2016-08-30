class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        def divider(a):
            if (a > 81):
                div = 10**(len(str(a))/2-1)
                return div
            else:
                return 2

            
        if ((num == 1) | (num == 4)):
            return True
        elif (num >= 9):
            shortener = divider(num)
            for i in range(3,(num/shortener+1)):
                if ((i*i) == num):
                    return True
        return False
