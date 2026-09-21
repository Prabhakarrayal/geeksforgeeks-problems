class Solution:
    def areAnagrams(self, root1, root2):
        from collections import Counter
        q1,q2=[root1],[root2]
        while q1 or q2:
            c1=Counter(x.data for x in q1 if x!=None)
            c2=Counter(x.data for x in q2 if x!=None)
            if c1!=c2:
                return False
            nq1,nq2=[],[]
            for n in q1:
                if n:
                    nq1.extend([n.left,n.right])
            for n in q2:
                if n:
                    nq2.extend([n.left,n.right])
            q1,q2=nq1,nq2
        return True