
 

#Metody zbiorow 

#q.intersection(a) # zwroci czesci wspolnej dwoch zbiorow lub print(q &a) (to samo) 
#q.union(a)  # q|a – zwroci calosc z obu zbiorow bez powtarzania  
#q.difference   q-a
#q.symetric_difference   q^a - zwroci roznice zbiorow
l.discard('q') #usnie pierwszy element 'q' z listy. Jesli go nie ma, nie zwroci bledu

s =  {'q', 'w', 'e', 'r', 't', 'y'}  # zbiory nie uporzadkowane ma stringi, ktory uzywa zegara systemowego. W petli wyswietli w  tej samej kolejnosci. 
s =  {'1', '2', '3', '4', '5', '6'}   #Natomiast liczby int same sie porzadkuja 

print(s)
s =  {*'qwerty'}  # zbiory nie uporzadkowane ma stringi, ktory uzywa zegara systemowego. W petli wyswietli w  tej samej kolejnosci
print(s)

s = {0, 1, 2, True}  #nie wypisze True, bo True to wartosc jeden, a juz jest wyswietlenie
print(s)
s = set('qwerty') # set na zbiory
print(s)


#zadanie slownik
word:str = input("Wpisz coś: ")
vocabulary = {
    "dog": "pies",
    "cat": "kot"   
}

print("napisałeś: ", vocabulary[word])


#zadanie losowanie liczby bez importa random 
a = {'1', '2', '3', '4', '5', '6'}
convlist = list(a)
print(convlist[0])


#zadanie wyswietlenie co dugi element listy
lista = [*"qwerty"]
for i in range(0, len(lista), 2):
    print(lista[i])
    
print(lista[::2]) #alternatywnie krócej 

