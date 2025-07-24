import json

# person = '{"name": "Hasan", "surname": "Kacar", "languages": ["python", "ASP", "Symfony", "JS", "PHP"]}'
# personArr = json.loads(person)
# name = personArr["name"]
# print(f"Name : {name}")



# with open("test.json") as f:
#     data = json.load(f)
#     print(data)



# personDict = {
#     "name": "Hasan",
#     "surname": "Kacar",
#     "languages": [
#         "Python",
#         "C#",
#         "PHP",
#         "Symfony"
#     ]
# }
#
# personJson = json.dumps(personDict)
# print(personJson)
#
# with open("person.json", "w") as f:
#     json.dump(personDict, f)



personDict = {
    "name": "Hasan",
    "surname": "Kacar",
    "languages": [
        "Python",
        "C#",
        "PHP",
        "Symfony"
    ]
}
personJson = '{"name": "Hasan", "surname": "Kacar", "languages": ["python", "ASP", "Symfony", "JS", "PHP"]}'
personArr = json.loads(personJson)
personJson2 = json.dumps(personArr, indent=4, sort_keys=True)

print(f"Person Arr : {personArr}")
print(f"Person JSON : {personJson2}")