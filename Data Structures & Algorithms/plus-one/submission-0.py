class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        whole_number = "".join(map(str, digits))
        plus = int(whole_number) + 1
        return list(map(int, str(plus)))