import copy
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = 0
        if len(prices) > 1:
            max_p = 0
            min_p = prices[0]
            temp = prices[0]
            
            for p in prices[1:]:
                
                if p < temp:
                    temp = p
                if p >= max_p or (p-temp)>(max_p-min_p):
                    max_p = p
                    min_p = copy.deepcopy(temp)
            if (max_p > min_p):        
                diff = max_p - min_p
            
        return diff