
            
            
            #zapis pliku 'r' 'w' - tworzy nowy plik jesli istnieje, czysci go 'a' - dopisuje do istniejacego pliku 
            # 'r+' read and write    na poczatku pliku 'w+' odczyt zapis, plik jest tworzony jesli nie istnieje i czysci istniejeacy
            # 'a+'dopisuje na koniec pliku, jesli nie istnieje plik, tworzy go
            
with open('tajne_dane.txt', 'a') as tajne_dane:
    
    tajne_dane.write('mail@mail.com\n')
        
        
        
#odczyt pliku
with open('tajne_dane.txt', 'r') as tajne_dane:
    
    if tajne_dane.readable():
        for linijka in tajne_dane.readlines():
            if linijka[0] == '#':
                continue # w pliku poczatki linijek # beda pomijane
            print(linijka.rstrip())