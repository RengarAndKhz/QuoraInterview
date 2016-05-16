class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        x = min(C, G)
        y = min(D, H)
        a = max(A, E)
        b = max(B, F)
        overlap = max(x - a, 0) * max(y - b, 0)
        return abs(C - A)*abs(D - B) + abs(G - E)*abs(H - F) - overlap