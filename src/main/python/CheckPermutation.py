'''
Check Permutation:
Given two strings, write a method to decide if one is a permutation of the
other.
'''

from typing import DefaultDict


def checkPermutation(s1:str,s2:str)->bool:
    if len(s1)!=len(s2):return False

    mem = DefaultDict(int) 
    for c in s1:
        mem[c] += 1
    
    for c in s2:
        if mem[c] == 0: return False
        else:mem[c] -= 1
    
    return True

def checkPermutation2(s1:str,s2:str)->bool:
    return sorted(s1) == sorted(s2)

if __name__ == '__main__':
    assert checkPermutation('abcd','dacb') == True
    assert checkPermutation('abcd','dacw') == False
    assert checkPermutation('','dacw') == False

    assert checkPermutation2('abcd','dacb') == True
    assert checkPermutation2('abcd','dacw') == False
    assert checkPermutation2('','dacw') == False



