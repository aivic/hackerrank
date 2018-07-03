N = int(input())
X = list(map(int, input().split()))
W = list(map(int, input().split()))

out = 0
for i in range(N):
    out += X[i] * W[i]
print(round(out/sum(W),1))
