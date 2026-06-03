class Solution:
    def addSpaces(self,space,l):
        j = 0
        ans =[]
        for i in range(len(space)):
            if j<len(l) and l[j] == i:
                ans.append(" ")
                j +=1
            ans.append(space[i])
        
        return ''.join(ans)