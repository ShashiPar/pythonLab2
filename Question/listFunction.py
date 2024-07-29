class ListFunctions:

    def findMax(self, n):
        return max(n)

    def findMin(self, n):
        return min(n)

    def sum(self, n):
        return sum(n)

    def avg(self, n):
        return sum(n) / len(n)

    def median(self, n):
        numbers = len(n)
        sorted_numbers = sorted(n)
        if numbers % 2 == 0:
            median = (sorted_numbers[numbers // 2 - 1] + sorted_numbers[numbers // 2]) / 2
        else:
            median = sorted_numbers[numbers // 2]
        return median
