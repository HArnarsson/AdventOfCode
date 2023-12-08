
from time import time

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
    return dp[n][summa]

start = time()
print(SS(containers, target))
print(time() - start)
