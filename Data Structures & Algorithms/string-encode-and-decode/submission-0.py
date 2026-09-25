class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            temp = str(len(i))
            res += temp + "#" + i
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = [] 

        while i < len(s):
            j = i 

            while s[j] != "#":
                j += 1

            length_str = int(s[i:j])  
            i = j+1

            word = s[i: i+length_str]
            res.append(word)

            i += length_str

        return res