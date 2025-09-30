import heapq

def min_costs(cables):
    if not cables:
        return 0

    heapq.heapify(cables)
    temp_costs = 0

    while len(cables) > 1:
        cost = heapq.heappop(cables) + heapq.heappop(cables)
        temp_costs += cost
        heapq.heappush(cables, cost)

    return temp_costs


# Test
cables = [7, 5, 8, 3, 2, 4]
print("Min total costs:", min_costs(cables))