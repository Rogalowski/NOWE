print("Podaj liczbe, sprawdzimy czy jest podzielna przez 7")

x = int(input())

if x%7 !=0:
    print("Nie OK")
else:
    print("OK")
    
    
    
    
weekDays    = {'pon':1,'wt':2,'sr':3,'czw':4,'pt':5,'sb':6,'nd':7}
dayNum      = input('Jaki dzień? ')
weekNum     = int(input('Który tydzien roku? '))-1
june1       = input('Jakim dniem był 1 stycznia? ')

print(weekDays[dayNum]+weekNum*7-weekDays[june1]+1)