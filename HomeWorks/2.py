'''
 1. İki ədədin yerini dəyişmək (başqa dəyişən istifadə etmədən)
 Tapşırıq: İstifadəçidən iki tam ədəd (
 a və b) daxil etməsini istəyin. Onların yerini
başqa dəyişən yaratmadan dəyişin və nəticəni ekrana yazdırın.
'''
a = 5
b = 7
a, b = b, a
print(a, b)

'''
2. Verilmiş indeksdəki simvolu dəyişmək
Tapşırıq: İstifadəçidən bir mətn, bir indeks və bir simvol daxil etməsini istəyin. 
Göstərilən indeksdəki simvolu daxil edilən simvol ilə əvəz edin. Unutmayın ki, 
string-lər dəyişməzdir, ona görə yeni string yaradılmalıdır.
'''
_str = input('insert your word: ')
index = _str[int(input('insert your index: '))]
new_symb = input('insert new symbol: ')
new_str = _str.replace(index, new_symb)
print(new_str)


# 3. String-in tərsini tapmaq
#  Tapşırıq: İstifadəçidən bir mətn daxil etməsini istəyin və onu tərsinə çevirin
_str = input()
reversed_str =_str[::-1]
print(reversed_str)


