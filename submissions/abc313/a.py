N = int(input())
p = list(map(int,input().split()))
result = 0

if N==1:
  pass
elif max(p) == p[0]:
  if sorted(p)[-2] == p[0]:
    result = 1
  pass
else:
  result = max(p)-p[0]+1

print(result)
