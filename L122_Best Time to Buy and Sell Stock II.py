import copy
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        total = 0
        flag = 0
        diff = 0
        if (len(prices)>1):
            temp_min = prices[0]
            temp_max = 0
            
            for p in prices[1:]:
                
                if (flag == 1) and (p < temp_max):
                    
                    total = total + diff
                    temp_min = p
                    flag = 0
                    diff = 0
                    
                elif (p < temp_min):
                    temp_min = copy.deepcopy(p)
                    
                elif (p-temp_min) > diff:
                    diff = p-temp_min
                    temp_max = copy.deepcopy(p)
                    flag = 1
                    
            total = total + diff
        
        return total