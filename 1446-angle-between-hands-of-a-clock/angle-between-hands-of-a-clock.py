class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hrAngle = 0.5 * (hour * 60 + minutes)

        # Minute hand moves 6 degrees per minute
        minAngle = 6 * minutes

        # Find the absolute difference between the two angles
        angle = abs(hrAngle - minAngle)

        # Return the smaller angle of the two possible angles
        return min(360 - angle, angle)
