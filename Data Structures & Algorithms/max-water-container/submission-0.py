class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max = 0
        for i in range(len(heights)-1):
            for j in range(i,len(heights)):
                volume = min(heights[i], heights[j]) * (j - i)
                if volume > max:
                    max = volume                
        return max