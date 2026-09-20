class Solution:
    def largestSubsquare(self, mat):
        n = len(mat)

        hor = [[0] * n for _ in range(n)]
        ver = [[0] * n for _ in range(n)]

       
        for i in range(n):
            h = hor[i]
            v = ver[i]
            prev_v = ver[i - 1] if i else None

            for j in range(n):
                if mat[i][j] == 'X':
                    h[j] = 1 + (h[j - 1] if j else 0)
                    v[j] = 1 + (prev_v[j] if i else 0)

        ans = 0

       
        for i in range(n - 1, -1, -1):
            h = hor[i]
            v = ver[i]

            for j in range(n - 1, -1, -1):
                size = min(h[j], v[j])

                
                while size > ans:
                   
                    if hor[i - size + 1][j] >= size:
                        
                        if ver[i][j - size + 1] >= size:
                            ans = size
                            break

                    size -= 1

        return ans