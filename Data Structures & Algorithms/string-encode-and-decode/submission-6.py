class Solution:
    
    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += (str(len(s)) + "#" + s)
        return result
    
    def decode(self, strs: str) -> List[str]:
        result = []
        i = 0

        while i < len(strs):
            start = i
            while(strs[i] != '#'):
                i += 1
            length = int(strs[start:i])
            
            start = i + 1
            i = start + length

            result.append(strs[start : i])

        return result
