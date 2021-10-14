import flask
from flask import Flask, render_template, jsonify, request,redirect,url_for
from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup
import json
import xmltodict
import sys
from datetime import datetime

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client.dbproject

@app.route('/')
def index():
    # kimp = flask.Respo
    # nse()
    # kimp.headers["Access-Control-Allow-Origin"] = "*"
    return render_template('1page2-.html')


#지역별 명소 데이터 api 가져오기
@app.route('/place',methods=['GET','POST'])
def show_place():

    #선택한지역 넘겨주기
    if request.method == 'POST':
        want = request.form.get('inputGroupSelect04')
        #print(want)
        places = db.sample.find({"area": want}, {'_id': False})

        places=list(places)

        return render_template('2page.html',data=want,places=places)

#명소의 자세한 페이지
@app.route('/detail',methods=['POST','GET'])
def show_detail():
    name = request.form['name_give']
    print(name)
    places = db.sample.find({"name": name}, {'_id': False})

    places = list(places)
    print(places)
    return {'result': places}


@app.route('/3page',methods=['GET'])
def show_detail2():
     name = request.args.get('name')
     #명소에 대한 정보 불러오기
     places = db.sample.find({"name": name}, {'_id': False})
     #명소에 대한 리뷰 불러오기
     # reviews= db.reviews.find({"where": name}, {'_id': False})
     #최신리뷰 3개만 3페이지에 나타나게
     reviews = list(db.reviews.find({"where": name}, {'_id': False}).sort([("reg_date", -1)]))
     places=list(places)
     reviews=list(reviews)
     if len(reviews)>3:
         reviews=reviews[0:3]
     print(reviews)
     return render_template('3page-.html',place=places,reviews=reviews)

#공공데이터 api query url 만드는함수
def get_request_query(url, operation, params, serviceKey):
    import urllib.parse as urlparse
    params = urlparse.urlencode(params)
    request_query = url + '/' + operation + '?' + params + '&' + 'serviceKey' + '=' + serviceKey
    return request_query

@app.route('/time',methods=['GET'])
def show_time():
    URL="http://apis.data.go.kr/B090041/openapi/service/RiseSetInfoService"
    OPERATION = 'getLCRiseSetInfo'
    SERVICEKEY="/oZ4AFQEH6WdKfRkiTxU9cNH8VHjxNsZO3PeRFfdDwIQLI3TfmMbjfQvhRSJyrACs3w1ARppFgEkiz5ebTfibg=="


    longitude = request.args.get('long',int)
    latitude = request.args.get('lati',int)
    date = request.args.get('date',int)
    PARAMS={
        'locdate':date,
        'longitude':longitude,
        'latitude':latitude,
        'dnYn':'y'

    }


    #response=requests.get("http://apis.data.go.kr/B090041/openapi/service/RiseSetInfoService/getLCRiseSetInfo?&longitude=" + longitude + "&latitude=" + latitude + "&locdate=" + date + "&dnYn=y&ServiceKey=/oZ4AFQEH6WdKfRkiTxU9cNH8VHjxNsZO3PeRFfdDwIQLI3TfmMbjfQvhRSJyrACs3w1ARppFgEkiz5ebTfibg==")
    request_query = get_request_query(URL, OPERATION, PARAMS, SERVICEKEY)

    response = requests.get(url=request_query)
    return response.text


@app.route('/reviewpage', methods=['GET'])
def go_reviews():
    place = request.args.get('place')

    want_reviews = list(db.reviews.find({'where':place}, {'_id': False}))

    return render_template('review.html', reviews=want_reviews,place=place)



## API 역할을 하는 부분
@app.route('/reviewpage', methods=['POST'])
def write_review():
    title_receive=request.form['title_give']
    where_receive = request.form['where_give']
    upload_receive = request.form['upload_give']
    print(upload_receive)
    review_receive = request.form['review_give']
    image_url='https://sparta-forposting.s3.ap-northeast-2.amazonaws.com/'+upload_receive

    doc = {
        'where':where_receive,
        'title':title_receive,
        'upload':image_url,
        'review':review_receive,
        'reg_date': datetime.now(),
    }
    db.reviews.insert_one(doc)

    return jsonify({'msg': '저장완료!'})

#
# @app.route('/reviewpage', methods=['GET'])
# def read_reviews():
#     go_reviews = list(db.reviews.find({}, {'_id': False}))
#
#     return jsonify({'all_reviews': go_reviews})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000,debug=True)