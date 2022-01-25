#Generator
x = (*(i**i for i in range(10)),) 
print(x)
# Generator yield w funkcji możemy rozpakowac print(*func()), czyli wyswieltic. Inaczej pokaze miejsce w pamieci. 

# List comprahenction: 

# Tworzenie listy na podstawie generatora x = [i for i in 'qwerty'] i x = {i for i in 'qwerty'} 

# Tworzenie krotki na podstawie generatora x = (*(i for i in 'qwerty'),) - po przecinku 

# X = [i+j for i in 'qwe' for j in 'asd']  - przemnozy każdy literke osobno przez drugi wyraz, jak przy zwykl. mnozeniu 

# X = [[i+j for i in 'qwe'] for j in 'asd']  - przemnozy każda literke koljeno z pierwszej listy do drugiej, tworzac osobno listy w liscie 


x = (i+j for i in (10,20,30) for j in (1,2,3))
print(*x)




x = (i+j for i in (10,20,30) for j in (1,2,3))
z = ([i+j for i in (10,20,30)] for j in (1,2,3))

y = []
for i in (10,20,30):
    for j in (1,2,3):
        y.append(i+j)
        
        
print(*x)
print(*z)
print(*y)




# #GENERATORY

# # x = (*(i for i in 'qwerty'),) 
# x = {i for i in 'qwerty'}
# x = [i+j for i in 'qwe' for j in 'asd']  # przemnozy każdy literke osobno przez drugi wyraz, jak przy zwykl. mnozeniu 
# x = [[i+j for i in 'qwe'] for j in 'asd']  #przemnozy każda literke koljeno z pierwszej listy do drugiej, tworzac osobno listy w liscie 

# print(x)

 


#Func
def f(n):
  for i in range(1,n+1):
      yield i
print(f(2))


lst = [1,2,3,4]
lst = lst[-3:-2]
lst = lst[-1]
print(lst)



s = 'abc'
for i in len(s):
  print(i)
  
  
def a(l,i):
  return l[i]


print(a((1,2),0))
0
1
2