class Solution:
    def dist(self, p1, p2):
        return (p2[0] - p1[0])**2 + (p2[1] - p1[1])**2

    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        distSet = {self.dist(p1, p2), 
        self.dist(p1, p3), 
        self.dist(p1, p4), 
        self.dist(p2, p3), 
        self.dist(p2, p4), 
        self.dist(p3, p4)}
        if len(distSet) == 2 and max(distSet) == 2*min(distSet):
            return True
        return False