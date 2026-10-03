
class Solution:

    def trap(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        water_level = 0
        water_amount = 0

        maximum = 0
        while l < r:
            minimum = min(heights[l], heights[r])
            if minimum > water_level:
                water_amount += (r - l - 1) * (minimum - water_level)
                water_level = minimum
                
            # print(l, r, water_level, water_amount)

            if heights[l] < heights[r]:
                l += 1
                if l < r:
                    water_amount -= min(water_level, heights[l]) 
            else:
                r -= 1
                if l < r:
                    water_amount -= min(water_level, heights[r]) 
        return water_amount
