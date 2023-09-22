class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        distance = [int(1e9)] * n

        distance[src] = 0

        for i in range(k+1):
            copy_distance = distance[:]
            for j in range(len(flights)):
                cur_node, next_node, cost = flights[j][0], flights[j][1], flights[j][2]

                if distance[cur_node] != int(1e9) and distance[cur_node] + cost < copy_distance[next_node]:
                    copy_distance[next_node] = distance[cur_node] + cost
            distance = copy_distance
        return distance[dst] if distance[dst] != int(1e9) else -1