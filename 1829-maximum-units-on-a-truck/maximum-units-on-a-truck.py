class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        print(boxTypes)
        boxTypes.sort(key=lambda boxType: boxType[1], reverse = True)
        res, currBox = 0, 0
        while truckSize > 0 and currBox < len(boxTypes):
            n = min(boxTypes[currBox][0], truckSize)
            res += boxTypes[currBox][1] * n
            truckSize -= n
            currBox += 1
        return res