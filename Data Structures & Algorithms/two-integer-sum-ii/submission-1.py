class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(0, len(numbers)):
            for n in range(i+1, len(numbers)):
                index_sum = numbers[i] + numbers[n]
                if index_sum == target:
                    return [i +1, n + 1]
        return []