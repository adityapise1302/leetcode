class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dirX, dirY = 0, 1
        x, y = 0, 0
        for inst in instructions:
            if inst == "G":
                x += dirX
                y += dirY
            elif inst == "L":
                dirX, dirY = -dirY, dirX
            else:
                dirX, dirY = dirY, -dirX
        return (x, y) == (0, 0) or (dirX, dirY) != (0, 1)
        
        