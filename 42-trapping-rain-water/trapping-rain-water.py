class Solution:
    def trap(self, height):
        n = len(height)
        l = [0] * n
        r = [0] * n
        lmax, rmax = 0, 0
        water = 0

        for i in range(n):
            # LEFT MAX
            lmax = max(lmax, height[i])
            l[i] = lmax

            # RIGHT MAX (same loop, reverse index)
            idx = n - 1 - i
            rmax = max(rmax, height[idx])
            r[idx] = rmax   # IMPORTANT FIX

        for i in range(n):
            water += min(l[i], r[i]) - height[i]

        return water