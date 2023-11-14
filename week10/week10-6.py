class Solution:
    def average(self, salary: List[int]) -> float:
        a = salary
        total = sum(a) - max(a) - min(a)
        N = len(salary) - 2
        return total / N

        #return ( sum(salary)-max(salary)-min(salary) ) / (len(salary)-2)    
