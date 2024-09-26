

def levenstein(str_1, str_2):
    n, m = len(str_1), len(str_2)
    if n > m:
        str_1, str_2 = str_2, str_1
        n, m = m, n

    current_row = range(n + 1)
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if str_1[j - 1] != str_2[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)

    distance = current_row[n]

    max_length = max(len(str_1), len(str_2))
    accuracy_percentage = (1 - distance / max_length) * 100

    return distance, accuracy_percentage

str1 = 'Привет мир'
str2 = 'Привет мир'
# 1 задание Петрова
print(f'Обычное сравнение\nПервое слово: {str1} \nВторое слово: {str2}')
print(levenstein(str1, str2))

# 2 задание Петрова

str1 = 'Привет мир'
str2 = 'Привет мир!'
print(f'\nЧастичное сравнение\nПервое слово: {str1} \nВторое слово: {str2}')
print(levenstein(str1, str2))

# 3 задание Петрова

str1 = 'Привет наш мир'
str2 = 'наш Привет мир'
print(f'\nСравнение по токену\nПервое слово: {str1} \nВторое слово: {str2}')
print(levenstein(str1, str2))

# 4 задание Петрова

str1 = 'Привет мир'
str2 = '!ПриВЕт, наш мир!'
print(f'\nПродвинутое обычное сравнение\nПервое слово: {str1} \nВторое слово: {str2}')
print(levenstein(str1, str2))

# 5 задание Петрова
str1 = 'Саратов'
city = ["Москва", "Санкт-Петербург", "Саратов", "Краснодар", "Воронеж", "Омск", "Екатеринбург", "Орск", "Красногорск", "Красноярск", "Самара"]



ans = sorted([[levenstein(str1, i), i] for i in city], key=lambda x: x[0])

print(f'\nСписок\nПервое слово: {str1} \n{ans}')


from fuzzywuzzy import fuzz, process

a = fuzz.ratio('Привет мир', 'Привет мир')
print(a)

a = fuzz.partial_ratio('Привет мир', 'Привет мир!')
print(a)

a = fuzz.partial_ratio('Привет мир', 'Люблю колбасу, Привет мир')
print(a)

a = fuzz.token_sort_ratio('Привет наш мир', 'мир наш Привет')
print(a)

a = fuzz.WRatio('Привет наш мир', '!ПриВЕт наш мир!')
print(a)

city = ["Москва", "Санкт-Петербург", "Саратов", "Краснодар", "Воронеж", "Омск", "Екатеринбург", "Орск", "Красногорск", "Красноярск", "Самара"]
a = process.extract("Саратов", city)
# Параметр limit по умолчанию имеет значение 5
print(a)


import datetime

str1 = 'SJSySzsubQRgsRpRpzmNaebZubfLNTzVxNsMcxaMzyWPHNKZLPOyWlbHczsStYMXIOKtYDZXBaWjSUejIaDHHotNBJVzEbwkPCCPoqFjmbewVmsOlJNUuSySrZAobwOCwXHMmmDcWRaTwICiAIvptiKbLJgAeMmkwzpUWnZlZtPgExyazBfbIfCTZTmRAMVYGBlakLHqTdNtaCgMEsCICILDpflRcZxNHJhZFkrBegNXjyWvlaRbjmKpkUQIDuHXJhLnNzxHaydGfeAHVWQTBKUelekxenTvQKBZLMDPbNoooJhvCdiYTneaIyfDUOBOTCtOKTbSSXiMzZYkalgVdjZGbefUIYqZiPzHiwdFLUcBIndfYtZPgJFAeRDVFgxWOiIRrGFMnqvrQObnuluSkFBOrPPVyMGgtBMcTHqlswfGiPeFvHSTJaCFUfwJKifnWlFfCyZkgEuLUpPDkrIIgjnvBlzRyuBAUbndLnISiGiDDJMnySJWFYkUcMHMTPAkFedSUNEXaPUwiiUXPKfAJSUjGCndVFYvWDbLjWMAAJRRYQnHvhwoBbOOXvwRuYdMPwdTEkpFZbrQRqSxHxyiZJYpjFxLZsnCNJZogrHgLAeOShDHvCdfsWDpPhFdTrTbAvmxwLxAvpJWjwQCFNXsnoAuTMoobRlrsfsPeNbghCNsDNGHBrfnBwguNYWbNFTJZfFlZsAcofxvHMNqAaOKpggyWTWrCXPKWWnnQnXlZwwOaoWUIqzOpePkSQGsPsctqjCrizWutYVlEbTDEayRxFqTiMfAObIRBZmPjxFfeMgwXRVNXQrVRjvBknPFkxiWSDmxvAjsdcphFFidqphuVpogihcKlaTcUGmlKqIefZuZZRSObasVlfoyeFgJNzWQOcYpXTRoHJWtsBnyDPKloAeIsNrIbcVYzcKepHpPtGQvtxEFbQMOZAhpawBslswMmhkuXgDpRlxwigmOUxVljPFexQUzvMyScUNUZuLV'
str2 = 'embRreaxrMWgrewXdIiNHHPGCUjWBwMqFvgFOAIfDdgjxQQbIfpjGgLXFmHWSOlqESkvcKQrBinTzqMIEJMSuQohbkoTqzzipFziusCRiHybJwDGByqLZxXsbNNvPfsmuQEeLhahNFVIgPQAEFMqGhQJbwaWJvywGmaMHGBwEPNxIWYsUkRsgtLErqpMhrlcKtIcZFNqgCisxuGqpbArFIeCjXhiQlrnMJgDFfJYcJpeAshliUEXSTfgeEEPxLSjpSDMfolgcGMMWQGaifExnyJUOYDxwpHDRMXMUixbefmbrFRuKuKenmKxcRDUHnutHfQkyUgVxUnLnjFVXCSTUlpcZPUGdngrEGEeMmEUZfSDWuAxfRSVVSKvjEcDljbeZqRdUQjbBCZMprOTrXCXPwdejixONMMWyIKxOeOWzTcrcVjjWKZJJAxkMmtCXQowsAWVlmJOpNpBOvZFdIplswxAlaNeabIwlXyZLjutXDFjwpSBxIrBzqjBYKjkKeIXNICitNBMgLXwWnEIqXsNItjFfeLucMnwpWfQFdVQPeikRUZBPPfVCCSfjNOzEIBJMcBgBayPHAscQYzNTHiJglLVwDdJyRCVuxUBMWFQZfScoPUAJxmKjvNLezOiSInRSGfxPDxMqoZJdyzlqEwPqORArRQyNGgapBnChfTKqrGLzVUKAyowWJcLximAzzAiuUUOHvRxpTCkMXfIVYtwzsedSnenGXoDJPHVZUExbmKxrlFHsNymwcqbMJJouQyQlhAbClvKiPosfYEJIQNUPECVJniNXnDIAQuGkmvYVLVflmHqEbjFQlCXmtjXLoBZdDluoyfUvffDgxLuhoZStbtwGwuvhbYPvuuycPVdzOdkLGIJKaVKXZNLvCWMxtiGHSMbWdkUrMChNCYpDWIeDVdEMHWwLiRvMSAOvYsmuMJvBONGuvNkaRAQqiRJTNWEkkSTkgamZcevwlnRBRdPRNXiBtZtqsgqyYUWhDQV'


start = datetime.datetime.now()
print(levenstein(str1, str2))
finish = datetime.datetime.now()
print('Время работы: ' + str(finish - start))



start = datetime.datetime.now()
a = fuzz.ratio(str1, str2)
finish = datetime.datetime.now()
print('Время работы: ' + str(finish - start)

print(a)