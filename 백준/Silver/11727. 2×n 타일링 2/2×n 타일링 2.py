import sys

n = int(sys.stdin.readline())

DP = []
DP.append(1)
DP.append(3)

for i in range(2, n):
    DP.append(DP[i-1] + 2 * DP[i-2])

print(DP[n-1] % 10007)