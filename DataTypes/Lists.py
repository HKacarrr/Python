from networkx import reverse

cars = ['BMW', 'Mercedes', 'Opel', 'Mazda']
print("Cars : ", cars)
print("Length of the cars : ", len(cars))
print("First item of the List : ", cars[0])
print("The last item of the List : ", cars[-1])

cars[3] = 'Toyota'
print("New Cars List : ", cars)

print("Mercedes is exist in the list : ", 'Mercedes' in cars)

print("-2 Index Value : ", cars[-2])

cars[-2:] = ['Toyota','Renault']
print("Cars : ", cars)

cars = cars + ['Audi', 'Nissan']
print("Cars : ", cars)

del cars[-1]
print("Cars : ", cars)
