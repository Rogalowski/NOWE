#krotsze
# sex     = 'mężczyzna'   if input('Płeć: ') == 'męska'               else 'kobieta'
# age     = 'dorosła/y'   if int(input('Wiek: ')) >= 18               else 'niepełnoletni/a'
# skin    = 'biała/y'     if input('Rasa: ') == 'kaukaska'            else 'kolorowa/y'
# country = 'Polka/lak'   if input('Kraj pochodzenia: ') == 'Polska'  else 'imigrant/ka'

# print(sex,age,skin,country)

sex     = input('Płeć: ') == 'męska'
age     = int(input('Wiek: ')) >= 18
race    = input('Rasa: ')
country = input('Kraj pochodzenia: ') == 'Polska'

sexTerm = 'mężczyzna'   if sex              else 'kobieta'
ageTerm = 'dorosły'     if sex and age      else 'dorosła'  if age      else 'niepełnoletni'    if sex else 'niepełnoletnia'
# skin  = 'biały'       if sex and race     else 'biała'    if race     else 'kolorowy'         if sex else 'kolorowa'
dicRace = {
    
    (True, 'Kaukaska')      : 'biały',  
    (False, 'Kaukaska')     : 'biała',
    (True, 'Mongoidalna')   : 'zółty',  
    (False, 'Mongoidalna')  : 'żółta',
    (True, 'Negroidalna')   : 'czarny', 
    (False, 'Negroidalna')  : 'czarna',
 
}
skin = dicRace[(sex,race)]
nation  = 'Polak'       if sex and country  else 'Polka'    if country  else 'imigrant'         if sex else 'imigrantka'

print(sexTerm,ageTerm,skin,nation)
