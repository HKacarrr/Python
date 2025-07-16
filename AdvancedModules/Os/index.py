import os
from datetime import datetime

operationSystemName = os.name
currentDir = os.getcwd()
os.chdir("/Users/hasankacar/Desktop/Python")
# os.mkdir("new-test")
# os.makedirs("new-test/deneme-2") # iç içe klasör oluşturma
osList = os.listdir()

print(f"Operation system name : {operationSystemName}")
print(f"Current Directory : {currentDir}")
print(f"OS List Directories : {osList}")


# fileLists = os.listdir()
# for file in fileLists:
#     print(f"File : {file}")
#
#     if file.endswith(".py"):
#         print(f"Python File : {file}")


connectionFile = os.stat("connection.py")
fileCreatedDate = datetime.fromtimestamp(connectionFile.st_ctime)
fileLastAccessDate = datetime.fromtimestamp(connectionFile.st_atime)
fileUpdatedDate = datetime.fromtimestamp(connectionFile.st_mtime)

print(f"Connection File Details : {connectionFile}")
print(f"Connection File Created At : {fileCreatedDate}")
print(f"Connection File Last Access At : {fileLastAccessDate}")
print(f"Connection File Updated At : {fileUpdatedDate}")



# os.system("test.exe") # dosyayı çalıştırır
# os.rename("old-directory-name", "new-directory-name") # klasör ismini değiştirir
# os.rmdir("deleted-dir") # Klasör silme işlemi
# os.removedirs("deleted-all-dirs") # Klasör içinde başka klasörlerde varsa hepsini siler. Hiyerarşik silme


indexFilePath = os.path.abspath("index.py")
dirName = os.path.dirname("/Users/hasankacar/Desktop/Python/AdvancedModules/Os/index.py")
sampleDirName = os.path.dirname(os.path.abspath("index.py"))
fileIsExist = os.path.exists("/Users/hasankacar/Desktop/Python/AdvancedModules/Os/index.py")
pathIsDir = os.path.isdir("/Users/hasankacar/Desktop/Python/AdvancedModules/Os")
pathIsFile = os.path.isfile("/Users/hasankacar/Desktop/Python/AdvancedModules/Os/index.py")
joinPaths = os.path.join("/Users/hasankacar/Desktop/Python/AdvancedModules/Os", "yeniii", "yeniiii2")
splitPaths = os.path.split("/Users/hasankacar/Desktop/Python/AdvancedModules/Os")
fileInfo = os.path.splitext("index.py")
fileName = fileInfo[0]
fileExtension = fileInfo[1]

print(f"File Path : {indexFilePath}")
print(f"File Dir Name : {dirName}")
print(f"File is exist : {fileIsExist}")
print(f"Path is dir : {pathIsDir}")
print(f"Path is file : {pathIsFile}")
print(f"Join Paths : {joinPaths}")
print(f"Split Paths : {splitPaths}")
print(f"File Info --> File Name : {fileName}  &&  File Extensioın : {fileExtension}")