class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        visited_nums = set()
        while n not in visited_nums:
            visited_nums.add(n)
            n = self.squared_sum(n)
            if n == 1:
                return True
        return False

    def squared_sum(self, n: int) -> int:
        sum = 0
        while n > 0:
            sum += (n % 10)**2
            n = n // 10
        return sum