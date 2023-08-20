import sys

M = int(input())
D = list(map(int,input().split()))

middle = int((sum(D)+1)/2)
sum_D = []

if M == 1:
  if D[0] == 1:
    print(M, D[0])
  else:
    print(M, middle)
  sys.exit()

for i in range(M):
  sum_D.append(sum(D[0:i+1]))
  if sum_D[i]+D[i+1] >= middle:
    if sum_D[i] == middle:
      mouth = i+1
      day = D[i]
    else:
      mouth = i+2
      day = middle - sum_D[i]
    print(mouth, day)
    sys.exit()

