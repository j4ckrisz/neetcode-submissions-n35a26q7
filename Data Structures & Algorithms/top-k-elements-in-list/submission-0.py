class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        mylist= dict()

        for i in nums:

            mylist[i] = mylist.get(i,0) +1
        
        bucket = [[] for _ in range(len(nums)+1) ]

        for num, freq in mylist.items():
            bucket[freq].append(num)


        res = []
        for freq in range(len(bucket)-1, 0, -1):

            for num in bucket[freq]:

                res.append(num)

                if k == len(res):

                    return res

