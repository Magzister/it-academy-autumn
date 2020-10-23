"""
Дан список стран и городов каждой страны.
Затем даны названия городов. Для каждого города укажите,
в какой стране он находится.
Входные данные
Программа получает на вход количество стран N.
Далее идет N строк, каждая строка начинается с названия страны,
затем идут названия городов этой страны.
В следующей строке записано число M,
далее идут M запросов — названия каких-то M городов, перечисленных выше.
Выходные данные
Для каждого из запроса выведите название страны,
в котором находится данный город.
"""


id_country = {}
city_id = {}
for i in range(int(input())):
    country, *cities = input().split()
    id_country[i] = country
    for city in cities:
        city_id[city] = city_id.get(city, [])
        city_id[city].append(i)

for i in range(int(input())):
    for idx in city_id[input()]:
        print(id_country[idx])
