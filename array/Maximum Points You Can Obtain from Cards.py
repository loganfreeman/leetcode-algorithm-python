class Solution(object):
    def maxScore(self, cardPoints, k):
        ss=sum(cardPoints[:k])
        ss_=ss
        if k==len(cardPoints):
            return ss
        for ii in range(1,k+1):
            ss_+=cardPoints[-ii]-cardPoints[k-ii]
            if ss_>ss:
                ss=ss_
        return ss
