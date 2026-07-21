class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        # print(len(mat))
        if len(mat) == 1:
            return mat[0][0]
        f = 0
        s = 0
        j = len(mat) - 1
        for i in range(len(mat)):
            f +=mat[i][i]
            if j != i:
                s +=mat[i][j]
            j -=1


        return f+s