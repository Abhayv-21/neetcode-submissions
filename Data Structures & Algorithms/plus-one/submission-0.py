class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        temp = []
        for i in digits:
            s += str(i)

        curr = int(s)
        curr += 1
        s2 = str(curr)

        for i in s2:
            temp.append(int(i))

        return temp