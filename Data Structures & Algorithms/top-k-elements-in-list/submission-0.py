class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num,0)+1
        freq_list = [[] for _ in range(len(nums)+1)] #Создали пустой список списков
        for num, freq in count.items():
            freq_list[freq].append(num) 
        res = []
        for freq in range(len(freq_list) - 1, 0, -1): 
            for num in freq_list[freq]: 
                res.append(num)
                if len(res) == k:
                    return res

        return res[:k]