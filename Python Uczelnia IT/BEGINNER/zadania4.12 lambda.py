

def name(a=1,b=2,c=3):
    return a+b*c


#DLA CHĘTNYCH: Napisz w dwóch wersjach: def i lambda potegowanie dwoch argumentow z dowch parametrow. jesli jeden arg drugi ma miec domyslnie 2
def power(m,n=2):
    return m**n
print(power(3))


#LAMBDA  lambda m,n=2 : m**n
def poower(n=2):
  return lambda m : m ** n

mydoubler = poower()

print(mydoubler(3))




#args przyjmuje krotki, wypisz kwadraty  
def x(*args):
    for i in args:
        print(i**2)

x(1,2,3)



#zadanie Napisz funkcję przyjmującą dowolną ilość argumentów i zwracającą ich sumę, minimum jeden argument
def func_suma(a, *args, b):
    wynik = 0
    for i in args:
        wynik += i
         # lub  for i in range(len(args)):
        # wynik += args[i]
    return  wynik + a + b

print("Suma: ", func_suma(2,4,5,b=6))


def print2(*args, end='/n', sep=' '): pass


#Napisz funkcję przyjmującą dowolną ilość argumentów i zwracającą ich sumę, bądź iloraz - w zależności od wartości parametru key.
def func_suma_iloczyn(*args, key):
    
    if key == '+':
        wynik = 0
        for i in args:
            wynik += i  
            
    elif key == '*':
        wynik = 1
        for i in args:
            wynik *= i
            
    else:
        wynik = "Zly parametr key"
 
    return wynik
        
print(f"Wynik obliczenia: ", func_suma_iloczyn(1,2,3,4, key="s"))
        
        
        