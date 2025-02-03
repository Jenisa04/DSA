from itertools import combinations

class Solution(object):
    def maximalNetworkRank(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        graph = collections.defaultdict(set)

        # building the graphs based on road connections
        for city1, city2 in roads:
            graph[city1].add(city2)
            graph[city2].add(city1)

        res = 0

        # checks all possible combinations of the graph cities
        for city1, city2, in combinations(graph.keys(), 2):
            hasConnect = 1 if city1 in graph[city2] else 0

            city1Connects = len(graph[city1])
            city2Connects = len(graph[city2])

            res = max(res, city1Connects + city2Connects - hasConnect)

        return res