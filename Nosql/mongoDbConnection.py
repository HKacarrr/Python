import pymongo
from bson import ObjectId
from numpy.ma.core import product
from pymongo.server_api import ServerApi


client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['python-app']

uri = "mongodb+srv://hasankacar:7E6mQ0v2bnS0R4GW@cluster0.r97j9hf.mongodb.net/python-app?retryWrites=true&w=majority&appName=Cluster0"
client = pymongo.MongoClient(uri, server_api=ServerApi('1'))

db = client['python-app']
collection = db['product']



# product = {"name": "Laptop", "price": 1500, "quantity": 5}
# result = collection.insert_one(product)
#
# print("Result : ", result)




# productList = [
#     {"name": "Laptop", "price": 5500, "quantity": 5},
#     {"name": "Phone", "price": 3500, "quantity": 8},
#     {"name": "Mouse", "price": 800, "quantity": 20},
#     {"name": "Keyboard", "price": 1000, "quantity": 20},
#     {"name": "Mousepad", "price": 300, "quantity": 20},
# ]
# result = collection.insert_many(productList)




# result = collection.find_one()
# result = collection.find() # Select * From
# result = collection.find({}, {"_id": 0, "name": 1, "price": 1}) # ID ve quantity değerleri gelmez. Eğer 1 ola ndeğerleri çıkarırsak default zaten 1 olur ve quantity de gelir. Ama eklediğimiz için quantity değerleri gelmez
# for i in result:
#     print(i)




# filter = {"name": "Laptop"} # Select * From product where name = 'Laptop'
# result = collection.find(filter)
# for i in result:
#     print(i)





# filter = {"_id": ObjectId("686575e5814f400e39f0a1c9")}
# result = collection.find_one(filter)
# print(result)




# filter = {"name": {
#     "$in": ["Laptop", "Phone"]
# }}
# result = collection.find(filter)
# for i in result:
#     print(i)




# filter = {"price": {
#     "$gt": 1500 # Greater than 1500
# }}
# filter = {"price": {
#     "$gte": 1500 # Greater than and equals >= 1500
# }}
# filter = {
#     "price": {
#         "$eq": 1500 # Equals 1500
#     }
# }
# result = collection.find(filter)
# for i in result:
#     print(i)




# filter = {"name": {
#     "$regex": "^L"  # Starts with L
# }}
# result = collection.find(filter)
# for i in result:
#     print(i)




# result = collection.find().sort("price", pymongo.DESCENDING) # Sort by price descending
# for i in result:
#     print(i)




# collection.update_one(
#     {'name': 'Keyboard'},
#     {'$set': {
#         'name': 'Keyboard New'
#     }}
# )


# query = {'name': 'Laptop'}
# newValues = {'$set': {
#     'name': 'Macbook Pro M3',
# }}
# collection.update_many(
#     query,
#     newValues
# )




# collection.delete_one({'name': 'Mousepad'})



# collection.delete_many({'name': {
#     '$regex': '^Mac'
# }})



collection.delete_many({})