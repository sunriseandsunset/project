#샘플데이터 - 강원도 3개 만들기
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client.dbproject

Gangwondo = [
        {"name": "하조대", "longtitude": 128.73568, "latitude": 38.02112},
        {"name": "남애항", "longtitude": 128.78742, "latitude": 37.94521},
        {"name": "정동진해변", "longtitude": 129.03455, "latitude": 37.69084},

]
db.sample.insert_many(Gangwondo)


