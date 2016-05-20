# 11. Container With Most Water

def maxArea(height):
    maxWater = 0
    l = 0
    r = len(height) - 1
    while l < r:
        shorter = min(height[l], height[r])
        maxWater = max(maxWater, shorter * (r-l))
        if shorter == height[l]:
            l += 1
        else:
            r -= 1
    return maxWater
