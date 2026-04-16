class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        l, r = 0, len(height) - 1
        left_max = right_max = water = 0
        
        while l < r:
            left_max = max(left_max, height[l])
            right_max = max(right_max, height[r])
            if height[l] < height[r]:
                water += (left_max - height[l])
                l += 1
            else:
                water += (right_max - height[r])
                r -= 1
        return water
