import copy

class Solution:
    
    def checkNearest(self, mat, m, n, call_no=1):
        row1 = [-1,-1,1,1]
        row1 = [i*call_no for i in row1]
        col1 = [-1,1,-1,1]
        col1 = [i*call_no for i in col1]
        row = [-1,0,0,1]
        row = [i*call_no for i in row]
        col = [0,-1,1,0]
        col = [i*call_no for i in col]
        #print(col)
        for k in range(len(row)):
            if 0 <= m+row[k] < len(mat) and 0 <= n+col[k] < len(mat[0]) and mat[m+row[k]][n+col[k]] == 0:
                print("here", call_no)
                return call_no
        for k in range(len(row1)):
            if 0 <= m+row1[k] < len(mat) and 0 <= n+col1[k] < len(mat[0]) and mat[m+row1[k]][n+col1[k]] == 0:
                print("here", call_no)
                return call_no+1
        print(m, n)
        return min(1+call_no*2, self.checkNearest(mat,m,n,call_no+1))

                    
    def updateMatrix(self, mat):
        #out_mat = [[0]*(len(mat))]*(len(mat[0]))
        rows, cols = (len(mat), len(mat[0]))
        out_mat = [[0 for i in range(cols)] for j in range(rows)] 
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] != 0:
                    #out_mat[i][j] = self.checkNearest(mat, i, j)
                    neighbors = []
                    for (d_r, d_c) in [(-1,0),(0,-1),(0,1),(1,0)]:
                        r = i + d_r
                        c = j + d_c
                        if rows > r >= 0 and cols > c >= 0:
                            neighbors.append(out_mat[r][c])
                    print(neighbors)
                    out_mat[i][j] = min(neighbors)+1 # DP Rule
        return out_mat

    def updateMatrixDP(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """

        nrows = len(matrix)
        nclms = len(matrix[0])
        cache = [[0] * nclms] * nrows
        output = copy.deepcopy(matrix)

        # loop until convergence
        while not cache.__eq__(output):
            cache = copy.deepcopy(output)
            for i in range(nrows):
                for j in range(nclms):
                    if output[i][j] != 0:
                        # find neighbors
                        neighbors = []
                        for (d_r, d_c) in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                            r = i + d_r
                            c = j + d_c
                            if nrows > r >= 0 and nclms > c >= 0:
                                neighbors.append(output[r][c])
                        # dp rule
                        output[i][j] = min(neighbors) + 1

        return output


#mat = [[1,0,1,1,0,0,1,0,0,1],[0,1,1,0,1,0,1,0,1,1],[0,0,1,0,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,1],[0,1,0,1,1,0,0,0,0,1],[0,0,1,0,1,1,1,0,1,0],[0,1,0,1,0,1,0,0,1,1],[1,0,0,0,1,1,1,1,0,1],[1,1,1,1,1,1,1,0,1,0],[1,1,1,1,0,1,0,0,1,1]]
#print(Solution().updateMatrix([[0,1,0],[0,1,0],[0,1,0],[0,1,0],[0,1,0]]))
mat = [[0,0,0],[0,1,0],[1,1,1]]
print(Solution().updateMatrixDP(mat))

##Submitted sol
class Solution:
	def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
		m = len(mat)
		n = len(mat[0])

		for i in range(m):
			for j in range(n):
				if mat[i][j] > 0:
					top = mat[i - 1][j] if i > 0 else math.inf
					left = mat[i][j - 1] if j > 0 else math.inf
					mat[i][j] = 1 + min(top,left)


		for i in range(m - 1, -1, -1):
			for j in range(n - 1, -1, -1):
				if mat[i][j] > 0:
					bottom = mat[i + 1][j] if i < m-1 else math.inf
					right = mat[i][j + 1] if j < n-1 else math.inf
					mat[i][j] = min(mat[i][j],bottom+1,right+1)
		return mat