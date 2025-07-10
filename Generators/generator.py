# def cube():
#     result = []
#
#     for i in range(5):
#         result.append(i ** 3)
#
#     return result


# Oluşturduğumuz değer anlık olarak kullanılıyorsa ve ileride kullanılmayacaksa bu şekişlde kullanmalıyız ve boşu boşuna bellekte tutmamalıyız.
# def cube():
#     for i in range(5):
#         yield i ** 3
#
# iterator = cube()
# print(next(iterator))



arrList = [i ** 3 for i in range(5)] # Çıktı : [0, 3, 8, 27, 64]
arrListIterator = (i ** 3 for i in range(5)) # Çıktı : <generator object <genexpr> at 0x10342f920>
print(arrListIterator)