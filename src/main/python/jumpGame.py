class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        
        cur = 0
        mx  = 0 
        l = len(s)
        
        q = deque()
        q.append(0)
        
        while q:
            cur = q.popleft()
            for i in range(max(cur + minJump,mx+1), min(cur + maxJump + 1,l)):
                if s[i] == '0':
                    if i == l-1: return True
                    q.append(i)
                nm = i
            mx = max(mx,cur + maxJump)
        
        return False