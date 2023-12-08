from time import time
from copy import deepcopy

containers = []

with open('input.txt', 'r') as file:
    for num in file:
        containers.append(int(num))

target = 150

def SS(containers, summa):
    # dp[i][j] represents the number of ways to sum j using containers[0:i], i not inclusive
    # Our solution will therefore be in dp[n][summa] at the end
    # Initialize bottom up table
    dp = [[0 for _ in range(summa+1)] for _ in range(len(containers) + 1)]
    # Base case: if we have an empty set but use all the numbers in the containers
    dp[0][0] = 1

    n = len(containers)
    # Base case: If we have the empty set but the remaining sum is not zero
    for i in range(1, summa + 1):
        dp[0][i] = 0
    # Recursive case: 
    for i in range(1, n+1):
        for j in range(summa+1):
            # If the remaining sum is greater than the last element, we can use that
            # => subtract it from the remaining sum if we do decide to include it
            # => don't subtract it from the remaining sum if we don't decide to include it
            # By doing it this way, we have a choice when containers[i-1] <= j
            # Either include the element or not. This will go through every case
            if containers[i-1] <= j:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-containers[i-1]]
            # If the remaining sum is lesser than the last element, we can't use that, go to the one before
            else:
                dp[i][j] = dp[i-1][j]
    return dp

# Now we want to find the ways to get target with the minimum number of containers
# The idea is to build up a parent pointer tree
# Start at dp[n][summa], if dp[i-1][j-containers[i-1]] != 0, add i to children of current
# Traceback to find the elements contributing to the target sum

def traceback(dp, summa, containers, n):
    subsets = []
    def backtrack(i, j, subset):
        # sum is 0 and we have reached the end of containers, valid subset
        if i == 0 and j == 0:
            # depcopy(subset) creates a copy, otherwise we keep using the same subset and overwrite it
            subsets.append(deepcopy(subset))
            return
        # This means that containers[i] was not selected, if dp[i-1][j] == 0, then there is no point continuing
        if i > 0 and dp[i - 1][j] != 0:
            backtrack(i - 1, j, subset)
        # This means that containers[i] was selected and it works, since dp[i - 1][j - containers[i - 1] != 0
        if i > 0 and j >= containers[i - 1] and dp[i - 1][j - containers[i - 1]]:
            subset.append(containers[i - 1])
            # Redo it with the new subset and different sum
            backtrack(i - 1, j - containers[i - 1], subset)
            # This is necessary so that we can backtrack and process other possibilities
            # If we reach this line then that means we did not return and it was not a valid possibility
            # Therefore, pop it off and keep going
            subset.pop()
    backtrack(n, summa, [])

    return subsets

dp = SS(containers, target)
n = len(containers)
subsets = traceback(dp, target, containers, n)
min_length = float('inf')

for subset in subsets:
    if len(subset) < min_length:
        min_length = len(subset)

count = 0
for subset in subsets:
    if len(subset) == min_length:
        count += 1

print(count)