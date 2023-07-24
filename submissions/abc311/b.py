import numpy as np

N,D = map(int,input().split())
string_list=np.array([list(input()) for i in range(N)])
result_c = 0
result = 0
result_old = 0


a = string_list[0]

for j in range(N-1):
  a = np.vstack([a,string_list[j+1]])
  

for i in range(D):
  if (N ==1):
      if(a[i]=='o'):
      	result_c+=1
      else:
        result_old = max(result_old,result_c)
        result_c = 0
      pass
  elif (all(x=='o' for x in a[:,i])):
    result_c+=1
  else:
    result_old = max(result_old,result_c)
    result_c = 0
    
result = max(result_old,result_c)  
print(result)
