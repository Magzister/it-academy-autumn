"""
Tuple practice
1. Создайте список ['a', 'b', 'c'] и сделайте из него кортеж.
2. Создайте кортеж ('a', 'b', 'c'), И сделайте из него список
3. Сделайте следующие присвоения одной строкой a = 'a', b=2, c=’python’.
4. Создайте кортеж из одного элемента, чтобы при итерировании по этому элементы
последовательно выводились значения 1, 2, 3.
Убедитесь что len() исходного кортежа возвращает 1.
"""

# 1
tpl = tuple(['a', 'b', 'c'])
print(tpl)
# 2
lst = list(('a', 'b', 'c'))
print(lst)
# 3
a, b, c = 'a', 2, 'python'
print(a, b, c)
# 4
tpl = ((1, 2, 3), )
for el in tpl:
    print(el)
print(len(tpl))
