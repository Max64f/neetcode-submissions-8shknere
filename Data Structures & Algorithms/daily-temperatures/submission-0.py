class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        stack = []
        res = [0] * len(t)
        for i in range(len(t)-1,-1,-1):
            while stack and t[stack[-1]]<= t[i]:
                stack.pop()
            if stack:
                res[i] = stack[-1] - i
            stack.append(i)
        return res