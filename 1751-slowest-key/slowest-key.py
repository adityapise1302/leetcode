class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        durations = [releaseTimes[0]]
        for i in range(1, len(releaseTimes)):
            durations.append(releaseTimes[i] - releaseTimes[i - 1])
        maxDurationChar = (0, '')
        for i, duration in enumerate(durations):
            if duration > maxDurationChar[0]:
                maxDurationChar = (duration, keysPressed[i])
            elif duration == maxDurationChar[0] and ord(maxDurationChar[1]) < ord(keysPressed[i]):
                maxDurationChar = (duration, keysPressed[i])
        return maxDurationChar[1]
