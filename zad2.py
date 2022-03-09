print('Kalkulator')
a = int(input('Pierwszą liczba'))
b = int(input('Drugą liczba'))
print('1. Dodawanie')
print('2. Odejmowanie')
print('3. Mnożenie')
print('4. Dzielenie')
wynik = 0
dzialanie = input('Działanie: ')
if dzialanie == '1':
    wynik = a + b
elif dzialanie == '2':
    wynik = a - b
elif dzialanie == '3':
    wynik = a * b
elif dzialanie == '4':
    wynik = a / b
else:
    wynik = 'Takie działanie nie obowiązuje'
print(wynik)