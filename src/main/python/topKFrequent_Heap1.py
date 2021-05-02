class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_counts = collections.Counter(words) 
        print(word_counts)
        arr = [(c,w) for w,c in word_counts.items()]
        return [x[1] for x in heapq.nsmallest(k, arr, key=lambda x: (-x[0],x[1]))]