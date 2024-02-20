class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        lst = [[1]]
        prev = [1]

        while len(lst) <= rowIndex:
            temp = [1]
            for i in range(len(prev)-1):
                temp.append(prev[i]+prev[i+1])
            temp.append(1)
            prev = temp
            lst.append(temp)
        return lst[-1]