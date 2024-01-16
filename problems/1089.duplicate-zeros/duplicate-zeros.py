class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        temp = []
        for num in arr:
            if num == 0:
                temp.append(0)
                temp.append(0)
            else: temp.append(num)
        
        for i in range(len(arr)):
            arr[i] = temp[i]
            