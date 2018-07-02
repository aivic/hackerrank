import numpy as np
from scipy import stats

X = int(input())
N = list(map(int, input().split()))
print(np.mean(N))
print(np.median(N))
print(stats.mode(N)[0][0])
