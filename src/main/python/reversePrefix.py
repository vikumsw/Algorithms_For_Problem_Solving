class Solution:

    def reversePrefix(self, word: str, ch: str) -> str:
        ll = len(word)
        ind = -1
        found = False
        for i in range(ll):
            if word[i]==ch:
                found = True
                ind = i
                break
        
        ret = word
        if found:
            ret = word[:ind+1][::-1] + word[ind+1:]
            
        return ret