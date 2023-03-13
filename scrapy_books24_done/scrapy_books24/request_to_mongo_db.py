from pymongo import MongoClient
import pprint 

clieent_TV = MongoClient('localhost:27017')
db = clieent_TV.books24

for document in db.books24.find({"genre" : "Зарубежное фэнтези", "author" : "Катажина Береника Мищук"}):
    print(document)