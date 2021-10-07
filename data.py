<<<<<<< HEAD
=======
#샘플데이터 - 강원도 3개 만들기
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client.dbproject

Gangwondo = [
        {"name": "하조대", "area":"강원도","longtitude": 128.73568, "latitude": 38.02112,"address":"강원도 양양군 현북면",'image':'https://search.pstatic.net/common?quality=75&direct=true&src=http%3A%2F%2Fthumb.photo.naver.net%2F20130916_110%2Fykahn007_1379286942805Q9B2U_JPEG%2F130916-3083-1.jpg'},
        # {"name": "남애항","area":"강원도", "longtitude": 128.78742, "latitude": 37.94521,"address":"강원도 양양군 현남면"},
        # {"name": "정동진해변", "area":"강원도","longtitude": 129.03455, "latitude": 37.69084,"address":"강원도 강릉시 강동면"},

]
db.sample.insert_many(Gangwondo)


>>>>>>> 957ff2f36a7adc6d3315e1913ac2eec2e7e64015
