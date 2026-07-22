class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        visited_nums = set()
        while n != 1:
            n = self.squared_sum(n)
            if n in visited_nums:
                return False
            visited_nums.add(n)
        return True

    def squared_sum(self, n: int) -> int:
        sum = 0
        while n > 0:
            sum += (n % 10)**2
            n = n // 10
        return sum