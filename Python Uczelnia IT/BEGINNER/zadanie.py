print("Podaj wiek")
x = input()

print("Podaj imie")
y =  input()



if int(x)>18 and y[-1]=='a':
    print ("Kobieta")
elif int(x)<18 and y[-1]=='a':
    print ("Dziewczyna")
elif int(x)<18:
    print ("Chlopak")
else:
    print ("Mezczyzna")