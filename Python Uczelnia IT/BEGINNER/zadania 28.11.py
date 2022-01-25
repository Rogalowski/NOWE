

# # czy podany znak to liczba? zadanie

# def strNumber(text):
#     for i in text:
#         if i in "1234567890":
#             x = True
#         else: 
#             x = False
#             break
#     return x

# def inputText():
#     text = input("Podaj znak: ")
#     print(strNumber(text))
          
# inputText()




# #Czy kobieta, dziewczyna, chlopak mezczyzna
# isAdult = False
# isFemale = False
 
# x = ( 'chłopak', 'mężczyzna', 'dziewczyna', 'kobieta' )
 
# print(x[ isAdult*1 + isFemale*2 ])


#DOMOWE
# Napisz program, który pobiera od użytkownika string zawierający dzień tygodnia i wyświetlający numer od 1 do 7.


# week_day = {
#     'ponidzialek': 1,
#     'wtorek': 2,
#     'sroda': 3,
#     'czwartek': 4,
#     'piatek': 5,
#     'sobota': 6,
#     'niedziela': 7
# }

# choose_day = input("Wybierz dzien tygodnia: ")

# while choose_day not in week_day:
#     choose_day = input("Nieprawidłowy dzien tygodnia, spróbuj jeszcze raz: ")

# print(f"Wybrałeś {choose_day}, a to jest dzień tygodnia nr: {week_day[choose_day]}")
# week_day.get(choose_day, "Nie prawidłowy dzień tygodnia")


# # Napisz program, który zaszyfruje string podany przez użytkownika w ten sposób, że najpierw wyświetli wszystkie znaki parzyste, a następnie wszystkie znaki nieparzyste.	
# user_text = input("Podaj tekst, który później zaszyfruję: ")
# # text = "abcdefghijklmnopqrstwxyz"
# list_text = list(user_text)
# even_text = []
# odd_text = []

# convertet_text = ''

# for i in range(0, len(list_text)):
#     if not i%2:
#         even_text.append(list_text[i])
#     else:
#         odd_text.append(list_text[i])
 

# for c in odd_text:
#     convertet_text += c
# for c in even_text:
#     convertet_text += c

    
# print(f"Oryginalny text: {user_text}")
# print(f"Zaszyfrowany text: {convertet_text}")
 



# # Napisz program sprawdzający czy string jest poprawną nazwą zmiennej w Pythonie. Zmienne mogą zawierać jedynie litery, cyfry i podłogę, nie mogą zaczynać się od cyfry i nie mogą być słowami kluczowymi. Lista słów kluczowych:

# keywords = ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
# numbers = ['0', '1', '2', '3','4', '5', '6', '7', '8', '9']
# # numbers = '0123456789'
# # variable = '2asr2uef'
# variable = input("Podaj nazwę zmiennej jaką chcesz wykorzystać: ")

# # def num_func(text):
# #     for c in range(len(variable)):
# #         if variable[c] in numbers:
# #             # 
# #             return True
 
 
# if variable in keywords: 
#     print("Nieprawidłowa nazwa zmiennej, zarezerwowana")
# elif " " in variable:
#     print("Nieprawidłowa nazwa zmiennej, ma spacje!")
# # elif num_func(variable) == True:
# elif variable[0] in numbers:
#     print("Nieprawidłowa nazwa zmiennej, posiada liczbę na początku")
# else:
#     print(f"Nazwa zmiennej: {variable}, jest OK!")
 
    
 
 
 
# Napisz program, który pobierze od użytkownika trzy imiona. 
# 		Jeżeli wszystkie imiona kończą się na 'a' lub 'A', niech program wyświetli 'dziewczęta'. 
# 		Jeżeli żadne z imion nie kończy się na 'a' lub 'A', niech program wyświetli 'chłopcy'.
# 		Jeżeli część imion kończy się na 'a' lub 'A', niech program wyświetli 'klasa mieszana'.

# miesz = ['Jacek', 'Ania', 'Marek']
# chlop = ['Jacek', 'pawel', 'Jakub']
# dziew = ['anna', 'patrycja', 'RoksanA']

sex_counter = 0
list_names = []
 

for i in range(3):
    name = input(f"Podaj imie nr{i}: ")
    list_names.append(name.strip())
    
    if 'a' in list_names[i][-1] or 'A' in list_names[i][-1] :
        # print("dziewczyna")
        sex_counter += 1
    else:
        # print("chlopiec")
        sex_counter -= 1


print(f"Podales imiona: {list_names}, a to są:")

if sex_counter == len(list_names):
    print("dziewczeta")
elif len(list_names) + sex_counter == 0:
    print("chlopcy")
else:
    print("ludzie roznych płci")
        