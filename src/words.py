"""
Во входной строке записан текст.
Словом считается последовательность
непробельных символов идущих подряд,
слова разделены одним или большим
числом пробелов или символами конца строки.
Определите, сколько различных слов содержится в этом тексте.
"""

str_ = ('abc abc abd abd  '
        '  abdd abddd abd anc \n a a a aaa '
        'a aaa aa aa \n \n \n abc abc')

set_ = set(str_.split())
print(*set_)
print('Всего слов - {}'.format(len(set_)))
