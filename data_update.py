#샘플데이터 - 강원도 3개 만들기
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client.dbproject

Gangwon = [
        {"name": "하조대", "address":"강원","longtitude": 128.73568, "latitude": 38.02112},
        {"name": "남애항","address":"강원", "longtitude": 128.78742, "latitude": 37.94521},
        {"name": "정동진해변", "address":"강원","longtitude": 129.03455, "latitude": 37.69084},
        {"name": "태백산", "address":"강원","longtitude": 128.5454, "latitude": 37.0544},
]

Seoul = [
        {"name": "하늘공원", "address":"서울","longtitude": 126.5308, "latitude": 37.3402},
        {"name": "선유도공원", "address":"서울","longtitude": 126.5358, "latitude": 37.3236},
        {"name": "아차산 정상", "address":"서울","longtitude": 126.0613, "latitude": 37.3417},
]

Incheon = [
        {"name": "민머루해수욕장", "address":"인천","longtitude": 126.2000, "latitude": 37.3839},
        {"name": "동막해수욕장", "address":"인천","longtitude": 126.2729, "latitude": 37.3533},
        {"name": "영종도", "address":"인천","longtitude": 126.4846, "latitude": 37.3205},
        {"name": "추암해수욕장", "address":"인천","longtitude": 129.0934, "latitude": 37.2839},
        {"name": "을왕리해수욕장", "address":"인천","longtitude": 126.2221, "latitude": 37.2651},
        {"name": "마시안해변", "address":"인천","longtitude": 126.2459, "latitude": 37.2554},
]

Ulleung = [
        {"name": "울릉도", "address":"울릉군","longtitude": 130.5136, "latitude": 37.3041},
        {"name": "독도", "address":"울릉군","longtitude": 131.5200, "latitude": 37.1434},
]

Gyeonggi = [
        {"name": "탄도항", "address":"경기","longtitude": 126.3841, "latitude": 37.1132},
        {"name": "궁평리마을", "address":"경기","longtitude": 126.4100, "latitude": 37.0658},
]

Chungnam = [
        {"name": "왜목마을", "address":"충남","longtitude": 126.3139, "latitude": 37.0248},
        {"name": "간월암", "address":"충남","longtitude": 126.2440, "latitude": 36.3613},
        {"name": "꽃지해안공원", "address":"충남","longtitude": 126.2006, "latitude": 36.2948},
        {"name": "마량포해돋이마을", "address":"충남","longtitude": 126.3007, "latitude": 36.0807},
]

Chungbuk = [
        {"name": "도담삼봉", "address":"충북","longtitude": 128.2038, "latitude": 36.5959},
]

Gyeongnam = [
        {"name": "우포늪", "address":"경남","longtitude": 128.2443, "latitude": 35.3259},
        {"name": "지리산 천왕봉", "address":"경남","longtitude": 127.4350, "latitude": 35.2013},
]

Gyeongbuk = [
        {"name": "부석사", "address":"경북","longtitude": 128.4025, "latitude": 36.5923},
        {"name": "망양정", "address":"경북","longtitude": 129.2447, "latitude": 36.5807},
        {"name": "삼사해상공원", "address":"경북","longtitude": 129.2259, "latitude": 36.2043},
        {"name": "호미곶", "address":"경북","longtitude": 129.3030, "latitude": 36.0351},
        {"name": "읍천항", "address":"경북","longtitude": 129.2826, "latitude": 35.4129},
        {"name": "혼신지", "address":"경북","longtitude": 128.4232, "latitude": 35.4008},
]

Jeonbuk = [
        {"name": "변산반도", "address":"전북","longtitude": 127.5310, "latitude": 35.4129},
        {"name": "채석강", "address":"전북","longtitude": 126.2757, "latitude": 35.3729},
        {"name": "곰소항", "address":"전북","longtitude": 126.3615, "latitude": 35.3509},
]

Jeonnam = [
        {"name": "도리포", "address":"전남","longtitude": 126.2023, "latitude": 35.0915},
        {"name": "순천만", "address":"전남","longtitude": 127.3031, "latitude": 34.5406},
        {"name": "향일암", "address":"전남","longtitude": 127.4814, "latitude": 34.3529},
        {"name": "남열해수욕장", "address":"전남","longtitude": 127.2912, "latitude": 34.3449},
        {"name": "세방낙조전망대", "address":"전남","longtitude": 126.0612, "latitude": 34.2624},
        {"name": "땅끝마을", "address":"전남","longtitude": 126.3137, "latitude": 34.1800},
        {"name": "완도타워", "address":"전남","longtitude": 126.4559, "latitude": 34.1838},
]

Ulsan = [
        {"name": "강양항", "address":"울산","longtitude": 129.2048, "latitude": 35.2325},
        {"name": "간절곶", "address":"울산","longtitud": 129.2139, "latitude": 35.2135},
]

Busan = [
        {"name": "죽성성당", "address":"부산","longtitude": 129.1454, "latitude": 35.1427},
        {"name": "다대포", "address":"부산","longtitude": 128.5758, "latitude": 35.0248},
]

Jeju = [
        {"name": "성산일출봉", "address":"제주","longtitude": 126.5632, "latitude": 33.2728},
]



db.sample.insert_many(Gangwondo)


