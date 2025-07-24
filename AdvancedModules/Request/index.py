import json
import requests

result = requests.get("https://jsonplaceholder.typicode.com/todos")
resultContent = result.text
data = json.loads(resultContent)

print(data[0]['title'])