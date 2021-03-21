class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1,l2,l3 = len(s1),len(s2),len(s3)
        sl = set()
        sl.add((0,0,0))
        if s3==s2==s1=="":
            return True
        
        while sl:
            p1,p2,p3 = sl.pop()
            while(p3<l3):
                if p1<l1 and p2<l2 and s3[p3]==s1[p1] and s3[p3]==s2[p2]:
                    sl.add((p1,p2+1,p3+1))
                    if p1< l1:
                        p1 += 1
                elif p1< l1 and s3[p3]==s1[p1]:
                    p1 += 1
                elif p2< l2 and s3[p3]==s2[p2]:
                    p2 += 1
                else:
                    break
                p3 += 1
                if p3==l3 and p1==l1 and p2==l2:
                    return True
        
        
        return False