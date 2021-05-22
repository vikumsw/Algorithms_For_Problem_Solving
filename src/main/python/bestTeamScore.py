class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        teammates = list(zip(ages, scores))
        teammates.sort()
        
        l = len(teammates)
        maxScores = list(map(lambda x: x[1] , teammates))
        
        for i in range(1,l):
            for j in range(0,i):
                if teammates[j][1] <= teammates[i][1]:
                    maxScores[i] = max(maxScores[i],teammates[i][1]+ maxScores[j])

        return max(maxScores)
