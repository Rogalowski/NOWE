
f={
  1: 's',
  2: 'sd'  
}
sd = f.keys()
print(list(sd))

 
 
 
for i in range(3):
  print(i)
else:
  print(i)
print('#ZBADAC')
  
t = [[3-i for i in range(3)] for j in range(3)]
s=0
for i in range(3):
  s+=t[i][i]
print(s)

my_list = [1,2,3]
for v in range(len(my_list)):
  my_list.insert(1, my_list[v])
print(my_list)

tup = (1,) + (1,)
tup = tup + tup
print("gg",tup)