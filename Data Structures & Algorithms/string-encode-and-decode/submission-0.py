class Solution:

    def encode(self, strs: List[str]) -> str:
        x = ''.join(f"{len(s)}#{s}" for s in strs)
        x += '~'
        return x

    def decode(self, s: str) -> List[str]:
        ret = []
        x = s[0]
        index = 0

        while x != '~':
            j = index
            while s[j] != '#':
                j+=1
            length = int(s[index:j])
            index = j+1
            ret.append(s[index: index + length])
            index += length
            x = s[index]
        
        return ret


