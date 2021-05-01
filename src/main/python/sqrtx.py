class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_counts = collections.Counter(words) 
        print(word_counts)
        arr = [(c,w) for w,c in word_counts.items()]
        arr.sort(key=lambda item: (-item[0], item[1]))
        return list(map(lambda x:x[1],arr))[:k]
