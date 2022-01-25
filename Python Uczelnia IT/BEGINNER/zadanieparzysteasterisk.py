# [09:19] Karol Kołodziejczyk - Trener
#     Napiszcie funkcję, która przyjmuje dowolną ilość argumentów (int) i domyślnie wyświetla tylko liczby podzielne przez liczbę 2. 
#     Niech jednak będzie możliwość zmiany tej liczby, żeby funkcja sprawdzała np. podzielność przez 3, 10, 21 - w zależności od tego co poda użytkownik.
 
x = range(int(input("Podaj liczbe: "))+1)
y = int(input("Podaj cyfre przez ktora maja byc podzielne liczby: "))

def a(*x, y = 2):
    print(*(i for i in x if i% y == 0))
    

a(*x)
a(*x, y = y)