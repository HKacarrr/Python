import json

import requests

apiKey = "2e1b13c2585e2729fa552507"
apiUrl = f"https://v6.exchangerate-api.com/v6/{apiKey}/latest/"

bozulanDoviz = input("Bozulan Döviz Türü : ") # USD
alinanDoviz = input("Alınan Döviz : ") # TRY
miktar = input(f"Ne kadar {bozulanDoviz} bozdurmak istiyorsunuz : ")

sonuc = requests.get(apiUrl + bozulanDoviz)
data = json.loads(sonuc.text)
conversionRates = data['conversion_rates']


print(f"1 {bozulanDoviz}  =  {conversionRates[alinanDoviz]} {alinanDoviz}")
print(f"{miktar} {bozulanDoviz} = {conversionRates[alinanDoviz] * int(miktar)} {alinanDoviz}")
