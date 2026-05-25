class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graphs = {c: set() for w in words for c in w}
        indegree = {c: 0 for c in graphs}

        for i in range(len(words) - 1):
            prev, curr = words[i], words[i + 1]
            prev_len, curr_len = len(prev), len(curr)
            min_len = min(prev_len, curr_len)

            if prev_len > curr_len and prev[:min_len] == curr[:min_len]:
                return ""
            
            for idx in range(min_len):
                if prev[idx] != curr[idx]:
                    if curr[idx] not in graphs[prev[idx]]:
                        graphs[prev[idx]].add(curr[idx])
                        indegree[curr[idx]] += 1
                    break
        
        q = [c for c in indegree if indegree[c] == 0]
        res = []

        while q:
            char = q.pop(0)
            res.append(char)
            for neighbor in graphs[char]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        
        return "" if len(res) != len(indegree) else "".join(res)


        