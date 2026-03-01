class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speed_arr = [(position[i], speed[i]) for i in range(len(position))]
        position_speed_arr.sort(key = lambda x: x[0], reverse=True)
        res = [position_speed_arr[0]]
        for i in range(1, len(position_speed_arr)):
            t1 = (target - res[-1][0]) / res[-1][1]
            t2 = (target - position_speed_arr[i][0]) / position_speed_arr[i][1]
            if t1 < t2:
                res.append(position_speed_arr[i])
        return len(res)