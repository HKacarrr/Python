# def showWords(word, count):
#     while count > 0:
#         print("Word : ", word)
#         count -= 1
#
# showWords("Hasan kacar", 5)


def transformToList(*params):
    paramList = []
    addParamToList(params, paramList)
    return paramList


def addParamToList(params, listContent):
    for param in params:
        listContent.append(param)


paramsList = transformToList(10, 20, 30, 'Hasan', 'Software Developer', 'Football')
print(paramsList)