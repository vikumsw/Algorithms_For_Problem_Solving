class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_counts = collections.Counter(words) 
        print(word_counts)
        arr = [(-c,w) for w,c in word_counts.items()]
        heapq.heapify(arr)
        return [heapq.heappop(arr)[1] for _ in range(k)]