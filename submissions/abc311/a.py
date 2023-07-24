n = int(input())
string = str(input())


a = string.find('A')
b = string.find('B')
c = string.find('C')
result_list = [a,b,c]
result = max(result_list)+1
 
print(result)
