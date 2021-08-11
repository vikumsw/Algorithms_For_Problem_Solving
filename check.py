#Find first of binary search implementaion


ll = [True,True,True,True,False,False,False,False,False]

#answer should be = 3

def firstTrueInd(ll):
    hi = len(ll)-1
    lo = 0
    while lo<=hi:
        mid = lo + (hi-lo)//2
        if ll[mid] == True:
            if (mid+1<len(ll) and ll[mid+1] == False) or mid == len(ll) - 1:
                print('index of last true = ',mid)
                return mid
            else:
                lo = mid + 1
        else:
            hi = mid - 1
    
    return -1

assert firstTrueInd(ll) == 3
assert firstTrueInd([True,True,True]) == 2
assert firstTrueInd([False,False,False]) == -2 , "should return -1"


    

