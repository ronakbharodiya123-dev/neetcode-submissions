from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        return [nums for nums , freq in count.most_common(k)]



from collections import Counter
class Solution:
    def topKFrequent (self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        return [nums for nums , freq in count.most_common(2)]