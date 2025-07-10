arrList = [1, 2, 3, 4, 5]
iterator = iter(arrList)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))


# while True:
#     try:
#         element = next(iterator)
#         print("Element of the list : ", element)
#     except StopIteration:
#         print("Iteration Error!!!")
#         break


class MyNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.end:
            x = self.start
            self.start += 1
            return x
        else:
            raise StopIteration



list = MyNumbers(10, 20)
for x in list:
    print("X : ", x)