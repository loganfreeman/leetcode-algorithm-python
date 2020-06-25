class Solution:
    def longestCommonSubsequence(self, A, B):
        if A == None or B == None:
            return
        lenA, lenB = len(A), len(B)
        C = self.LCSLength(A, B)
        lcs = self.printLCS(C, A, B, lenA, lenB)
        return lcs

    def LCSLength(self, A, B):
        lenA, lenB = len(A), len(B)
        C = [[0]*(lenB+1) for i in range(lenA+1)]
        for i in range(1, lenA+1):
            for j in range(1, lenB+1):
                if A[i-1] == B[j-1]:
                    C[i][j] = C[i-1][j-1] + 1
                elif C[i-1][j] >= C[i][j-1]:
                    C[i][j] = C[i-1][j]
                else:
                    C[i][j] = C[i][j-1]
        return C
    def printLCS(self, arr, A, B, lenA, lenB):
        if lenA == 0 or lenB == 0:
            return ""
        if A[lenA-1] == B[lenB-1]:
            s = self.printLCS(arr, A, B, lenA-1, lenB-1) + A[lenA-1]
        elif arr[lenA-1][lenB] >= arr[lenA][lenB-1]:
            s = self.printLCS(arr, A, B, lenA-1, lenB)
        else:
            s = self.printLCS(arr, A, B, lenA, lenB-1)
        return s

s = Solution()
print(s.longestCommonSubsequence("ABCBDAB", "BDCABA"))