class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        '''
        Cards are arranged in rows, each card having an associated number of points.
        CardPoints denote the array containing the points cards.
        In One step we can take one card from the beginning or from the end
        of the row. We have to take exaclty k cards.
        We need to return the maximum score that we can obtain
        '''
        n=len(cardPoints)
        for i in range(1,n):        #calculate prefix sum array
            cardPoints[i] += cardPoints[i-1]
            
        window_size = n-k  
        
        rem_sum = cardPoints[n-k-1]      #slide window from beginning of array. So consider it as remaining sum array
        
        left=1
        right=n-k
        
        while (right<n):
            
            rem_sum = min(rem_sum,cardPoints[right]-cardPoints[left-1])
            right+=1
            left+=1
            
        return cardPoints[-1]-rem_sum
        