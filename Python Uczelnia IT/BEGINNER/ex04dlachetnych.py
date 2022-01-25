lista = ['grzuszki','mydło','bułki','ser']

biedra = 	 ['mydło','ser','schabowy','piwo']
warzywniak = ['gruszki','ogóry','kalarepa','pomidory']
spolem = 	 ['piwo','wino','wóda','fajki']
piekarnia =  ['bułki','chleb','pączki']

# Napisz program, wyświetlający użytkownikowi listę zakupów i pytający użytkownika,
# do jakiego sklepu idzie i usuwający z listy zakupów rzeczy dostępne w sklepie.
# Niech program pyta użytkownika o sklep, aż użytkownik nie "kupi" wszystkich rzeczy z listy

 

zakupy = [*'ASDFGHJKKLL']
while zakupy.count !=0:
    print(zakupy)
    x = input("Podaj literke do usuniecia: ")
    y = zakupy.index(x)
    zakupy.pop(y)

print(zakupy)