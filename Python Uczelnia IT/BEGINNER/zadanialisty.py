#usuwa z listy

zakupy = [*'ASDFGHJKKLL']
while zakupy.count !=0:
    print(zakupy)
    x = input("Podaj literke do usuniecia: ")
    y = zakupy.index(x)
    zakupy.pop(y)

print(zakupy)