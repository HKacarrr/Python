import re

sentence = "Python Education : Mid Level Education | 40 Hours"


# result = re.findall("Python", sentence)
# print(f"Count of the Pytthon word in the sentence : {len(result)}")



# result = re.split(" ", sentence)
# print(f"Result : {result}")



# result = re.sub(" ", "-", sentence)
# result = re.sub("\s", "-", sentence)
# print(result)



# result = re.search("Python", sentence)
# print(f"Result : {result}")
# print(f"Result Span : {result.span()}")
# print(f"Result Start : {result.start()}")
# print(f"Result End : {result.end()}")
# print(f"Result Group : {result.group()}")
# print(f"Result String : {result.string}")




# result = re.findall("[abc]", sentence) # a-b-c değerlerini arar
# print(f"Result : {result}")


# result = re.findall("[sat]", sentence) # s-a-t değerlerini arar
# print(f"Result : {result}")


# result = re.findall("[a-d]", sentence) # a-b-c-d değerlerini arar. A-D arası gibi
# print(f"Result : {result}")


# result = re.findall("[1-5]", sentence) # 1-2-3-4-5 değerleri arar. 1-5 arası gibi
# print(f"Result : {result}")


# result = re.findall("[^abc]", sentence) # a-b-c değerleri dışındaki karakterleri arar.
# print(f"Result : {result}")


# result = re.findall("...", sentence) # 3 karakterli değerleri arar. Pyt, hon, ed, uca, tio
# print(f"Result : {result}")


# result = re.findall("Py..on", sentence) # Py ile başlayıp on ile biten kelimeleri yakalar
# print(f"Result : {result}")


# result = re.findall("^Pyt", sentence) # Cümle Pyt ile başlıyorsa döndürür.
# print(f"Result : {result}")


# result = re.findall("ours$", sentence) # Cümle ours ile bitiyorsa döndürür.
# print(f"Result : {result}")


# result = re.findall("ho*urs", sentence) # Hooours ✅,  Hours ✅, Hurs ❌ o en az bir veya daha fazla olursa bulur
# print(f"Result : {result}")


# result = re.findall("h?urs", sentence) # Hooours ❌, Hours ✅, Hurs ✅  Hours üzerinden gidersek o yoksa veya 1 kere varsa bulur.
# print(f"Result : {result}")


# result = re.findall("[0-9]{2,4}", sentence) # en az 2 en fazla 4 basamaklı olan sayıları bulur
# print(f"Result : {result}")


# result = re.findall("\d", sentence) # Sayısal değer filtrelemesi
# print(f"Result : {result}")
