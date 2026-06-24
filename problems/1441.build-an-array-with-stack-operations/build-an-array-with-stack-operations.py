class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ops = []
        i = 0
        for num in range(1, n + 1):
            if i == len(target):
                break
            if num == target[i]:
                ops.append("Push")
                i += 1
            else:
                ops.append("Push")
                ops.append("Pop")
        return ops