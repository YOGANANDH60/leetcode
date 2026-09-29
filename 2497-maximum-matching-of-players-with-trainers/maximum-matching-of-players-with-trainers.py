class Solution:
    def matchPlayersAndTrainers(self, players: list[int], trainers: list[int]) -> int:
        players = sorted(players)
        trainers = sorted(trainers)

        i = 0
        j = 0
        while i<len(players) and j<len(trainers):
            if players[i] <= trainers[j]:
                i +=1
            j +=1

        return i
