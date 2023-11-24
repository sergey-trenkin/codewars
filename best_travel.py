# John and Mary want to travel between a few towns A, B, C ... Mary has on a sheet of paper a list of distances between these towns. ls = [50, 55, 57, 58, 60]. John is tired of driving and he says to Mary that he doesn't want to drive more than t = 174 miles and he will visit only 3 towns.

# Which distances, hence which towns, they will choose so that the sum of the distances is the biggest possible to please Mary and John?


from itertools import combinations

def choose_best_sum(t, k, ls):
    result = 0
    for c in combinations(ls, k):
        if sum(c) <= t:
            result = max(result, sum(c))
    if result == 0:
        return None
    return result 
