class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        
        max_age, max_bits = max(ages), max(ages).bit_length()
         
        max_scores = [[0] * ((max_age >> sh) + 1) for sh in range(max_bits)] # This is the enhanced search engine
        
        for score, age in sorted(zip(scores, ages)): 

            best_score = max([max_scores[0][age]] + [max_scores[sh][(age >> sh) - 1] for sh in range(age.bit_length())])
            for sh in range(max_bits): max_scores[sh][age>>sh] = max(max_scores[sh][age>>sh], score + best_score)
                
        return max(max_scores[0])