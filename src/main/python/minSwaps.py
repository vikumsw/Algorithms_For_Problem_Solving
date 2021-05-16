class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        lenght = len(s)
        count=0
        ones = s.count("1")
        zeros = lenght - ones
        if not abs(zeros - ones) < 2:
            return -1

        if zeros>ones:
            start = ["0"]
        elif zeros<ones:
            start = ["1"]
        else:
            start = ["0","1"]

        mincount = 99999999
        for si in start:
            count = 0
            next = si
            for i in range(lenght):
                if s[i]!=next:
                    count+=1
                next = "0" if next=="1" else "1"

            if count<mincount:
                mincount=count

        return int(mincount/2)

        
