class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        ans = []
        curr = ""

        phone = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        def backtrack(index):
            nonlocal curr
            if index == len(digits): 
                ans.append(curr) 
                return 

            digit = digits[index]

            if digit in phone:
                for i in phone[digit]:
                    curr += i
                    backtrack(index+1)
                    curr = curr[:-1]

        backtrack(0)
        return ans           