class DetectSquares:

    def __init__(self):
        self.points = defaultdict(int)
        self.dx = defaultdict(list)
        
    def add(self, point: List[int]) -> None:
        tup = (point[0],point[1])
        self.points[tup]+=1
        self.dx[point[0]].append(tup)
        
    def count(self, point: List[int]) -> int:
        x = point[0]
        y = point[1]
        tup = (x,y)
        c = 0
        for px in self.dx[x]:
            xy=px[1]
            l=abs(y-xy)
            if(l<=0):
                continue
                
            p1 = (x-l,y)
            p2 = (x-l,px[1])
            
            p3 = (x+l,y)
            p4 = (x+l,px[1])
            
            c +=self.points[p1]*self.points[p2]+self.points[p3]*self.points[p4]
        
        return c


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)