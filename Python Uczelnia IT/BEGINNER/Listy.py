l = list('qwerty')
#METODY LISTY

print(l.count('q')) #zwraca ilosc elementow w krotce l
print(l.index('q')) #zwraca pod jakim indexem skrywa sie pierwszy element q w krotce l

l.append('u') #dodaje element
l.insert(4, 'Q') # dodaje elemet 'Q' do listy l, przed elementem o index 4, jesli na koniec chcemy to uzywamy meotdy len() 
x = l.pop() #usuwa z listy l zwraca element o podanym index (domyslnie -1) 
l.sort() #sortuje liste alfabetycznie, lub od min do max
l.clear() #usuwa wszystkie lementy listy 
l.remove('q') #sunie pierwszy element 'q' z listy  


# Niech użytkownik wprowadzi dwie liczby, a program napisze, która z nich jest większa.
x = int(input('podaj pierwszą liczbę: '))
y = int(input('podaj drugą liczbę: '))
if x>y:
    print(x)
else:
    print(y)
    
    
#wyswietlenie liczb parzystych przy pomocy asteriksa rozpakowywacza
print(*range(0, 100+1, 2))



#wyswietlenei liczb parzystych i nie parzystych w liscie po podaniu ich przez uzytkownika

odd = []
even = []
x = input()

while x !='end':
    x2 = int(x)
    if x2%2: odd.append(x2)
    else:    even.append(x2)
    x = input()
    
print('odd: ', odd)
print('even: ', even)



#usuwanie z listy  0 zer
list_num = [1,2,0,0,2,0,0,3,2,0,1,6]
 
lenght = list_num.count(0)
list_non_zero = [list_num.pop(list_num.index(0)) for i in range(lenght)]
print(list_num)

fruits = ['apple', 'bannana', ' cherry']
fruits.remove('apple')
print(fruits)







#sortowanie dwoch liczb
print("podaj dwie liczby: ")
number = []
for i in range(2):
    number.append(input())  #parsujemy na int zeby dobrze posortowalo liczby

print(sorted(number)[-1])

#lub

x = int(input('podaj pierwszą liczbę: '))
y = int(input('podaj drugą liczbę: '))
if x>y:
    print(x)
else:
    print(y)