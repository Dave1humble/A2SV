class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses = collections.Counter()
        players = set()
        for winner, loser in matches:
            losses[loser] += 1
            players.add(winner)
            players.add(loser)
        one_lose, zero_lose = [], []
        for player in players:
            if losses[player] == 0:
                zero_lose.append(player)
            elif losses[player] == 1:
                one_lose.append(player)
        return [sorted(zero_lose), sorted(one_lose)]
