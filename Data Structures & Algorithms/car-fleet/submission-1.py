class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        loc = []

        for i in range(len(position)):
            loc.append((position[i], speed[i]))

        loc = sorted(loc, reverse=True)

        for i in range(len(loc)):
            curr_time = (target-loc[i][0])/loc[i][1]
            if len(stack) == 0:
                stack.append(curr_time)

            elif curr_time <= stack[-1]:
                continue
            else:
                stack.append(curr_time)

        return len(stack)