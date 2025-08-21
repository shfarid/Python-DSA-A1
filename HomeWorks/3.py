
# istifadəcidən yaşini soruşan program yazin. Əgər yaş 18-dən kicikdirsə "$agird",
# 18-25 aralıgindadirsa "Tələbə", 25-dən böyükdürsə "Məzun" sözünü cap etsin.
'''
year = int(input())

if year > 25:
  print('Student')
elif 18 <= year  <= 25:
  print('Mezun')
else:
  print('Shagird')
'''

# Sistemdə gizli parol "python123" saxlanilir. istifadəci parolu daxil edir. Əgər düzgün parolu daxil
# edərsə "Daxil oldunuz", əks halda "Səhv parol" cap olunsun.

'''
user_pass = input()
password = 'python123'

if user_pass == password:
  print('Welcome')
else:
  print('Wrong password')
'''

# istifadəcidən bir ədəd alin. Əger adad 3-3 bölünürsa "Fizz", 5-3 bölünürse "Buzz", 15-ə bölünürsə
# "FizzBuzz", əks halda sadəcə ədədin özü çap olunsun.

'''
number = int(input())

if number % 15 == 0:
  print('FizzBuzz')
elif number % 5 == 0:
  print('Buzz')
elif number % 3 == 0:
  print('Fizz')
else:
  print(number)

'''

# istifadəcidən 1-7 arasi rəqəm alin. Rəqəmə uygun həftə gününü (1 -> Bazar ertəsi, 7 -> Bazar)
# match-case istifadə edərək çap edin.
'''

'''

'''
week_day = int(input())

match week_day:
  case 1 | 2 | 3 | 4 | 5:
    print('workday')
  case 6 | 7:
    print('weekend')
  case _:
    print('No_matches')
'''


# istifadəcidən işiaforun rəngini (qirm1z1, sar1, yaş1l) soruşun.
# match-case istifadə edərək:qirmizi > "Dayan", sari - "Hazir ol", yaşil "Get" çIxIşini verən proqram yazin.

'''
color = input('insert color please: ')

match color.lower():
  case 'red':
    print("Stop")
  case 'yellow':
    print('Ready')
  case 'green':
    print('Go')
'''

# Sistemdə dostlar siyahisi var: ["Aysel", "Elvin", "Nigar"] . istifadəci ad daxil edir. Əgər ad
# siyahida varsa "Salam köhnə dost!", yoxdlursa "Tanimadim siz.." yazilsin.

'''
user_name = input()
names = ['Aysel', 'Elvin', 'Nigar']

if user_name.capitalize() in names:
    print('My dear friend')
else:
    print('I do not know you')
'''
