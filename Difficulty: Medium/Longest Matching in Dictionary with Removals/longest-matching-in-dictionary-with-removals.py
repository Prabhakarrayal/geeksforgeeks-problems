class Solution:
    def findLongestWord(self, s: str, d: list) -> str:
            from bisect import bisect_left
            from heapq import heapify, heappop
            s_ids = [[] for _ in range(26)]
            for i, c in enumerate(s):
                ci = ord(c) - ord('a')
                s_ids[ci].append(i)
            h = [(-len(word), word) for word in d]
            heapify(h)
            while h:
                _, word = heappop(h)
                i = 0
                for c in word:
                    ci = ord(c) - ord("a")
                    j = bisect_left(s_ids[ci], i)
                    if j == len(s_ids[ci]):
                        break
                    else:
                        i = s_ids[ci][j] + 1
                else:
                    return word
            return ""