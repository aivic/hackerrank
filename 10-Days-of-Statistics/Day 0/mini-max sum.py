#!/bin/python3

import itertools as it

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    variations = list(it.combinations(arr,4))
    m1 = 0; m2 = sum(variations[0])
    for i in range(len(variations)):
        if sum(variations[i]) > m1:
            m1 = sum(variations[i])
        if sum(variations[i]) <= m2:
            m2 = sum(variations[i])
    print(m2, m1)
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
