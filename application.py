import flask
import boto3
from flask_cors import CORS
import os
from flask import Flask, render_template, jsonify, request,redirect,url_for,flash
from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup
import json
import xmltodict
import sys

import jwt
import datetime
import hashlib
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta


application = Flask(__name__)
cors = CORS(application, resources={r"/*": {"origins": "*"}})
SECRET_KEY = (os.environ.get("SECRET"))

# client = MongoClient('localhost', 27017)
client = MongoClient(os.environ.get("MONGO_DB_PATH"))

db = client.dbproject

@application.route('/')
def index():
    return render_template('1page2-.html')

@application.route('/index')
def index2():
    #return render_template('1page2-.html')
    token_receive = request.cookies.get('mytoken')
    print(token_receive)
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        user_info = db.users.find_one({"username": payload["id"]},)
        username=user_info['username']
        popular = list(db.sample.find({}, {'_id': False}).sort([("heart_count", -1)]).limit(5))
        print(popular)
        return render_template('1page2-.html', username=username,token=token,places=popular)
    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="로그인 정보가 존재하지 않습니다."))
    except:
        return render_template('1page2-.html')







@application.route('/sign_in', methods=['POST'])
def sign_in():
    # 로그인
    username_receive = request.form['username_give']
    password_receive = request.form['password_give']

    pw_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    result = db.users.find_one({'username': username_receive, 'password': pw_hash})

    if result is not None:
        payload = {
         'id': username_receive,
         'exp': datetime.utcnow() + timedelta(seconds=700)  # 로그인 24시간 유지
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

        return jsonify({'result': 'success','token': token})
    # 찾지 못하면
    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})

# 로그인 페이지
@application.route('/login', methods=['GET'])
def login():
    msg = request.args.get("msg")
    return render_template('login.html', msg=msg)


# 회원가입
@application.route('/sign_up/save', methods=['POST'])
def sign_up():
    username_receive = request.form['username_give']
    password_receive = request.form['password_give']
    password_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    doc = {
        "username": username_receive,                               # 아이디
        "password": password_hash,                                  # 비밀번호
        "profile_name": "",
        "profile_pic": "",                                          # 프로필 사진 파일 이름
        "profile_pic_real": "profile_pics/profile_placeholder.png", # 프로필 사진 기본 이미지
        "profile_info": ""                                          # 프로필 한 마디
    }
    db.users.insert_one(doc)
    return jsonify({'result': 'success'})


# 아이디 중복확인
@application.route('/sign_up/check_dup', methods=['POST'])
def check_dup():
    username_receive = request.form['username_give']
    exists = bool(db.users.find_one({"username": username_receive},{'_id': False}))
    return jsonify({'result': 'success', 'exists': exists})

# 마이페이지
@application.route('/mypage', methods=['GET'])
def mypage():
    token_receive = request.cookies.get('mytoken')
    print('mypage 서버에서 받는 토큰',token_receive)
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        user_info = db.users.find_one({"username": payload["id"]},{'_id': False})
        username=user_info['username']
        reviews = list(db.reviews.find({"writer": username}, {'_id': False}).sort([("reg_date", -1)]))
        #사용자가 찜한 하트보기
        heart_place = list(db.heart.find({"username": username}, {'_id': False}).sort([("reg_date", -1)]))
        print(heart_place)
        return render_template('mypage.html', username=username,reviews=reviews,heart_place=heart_place,token=token)

    except (jwt.exceptions.DecodeError,jwt.ExpiredSignatureError):
        flash('로그인을 해주세요!')
        return render_template("login.html")






#지역별 명소 데이터 api 가져오기
@application.route('/place',methods=['GET','POST'])
def show_place():
    token_receive = request.cookies.get('mytoken')
    print('2page 서버에서 받는 토큰', token_receive)
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        user_info = db.users.find_one({"username": payload["id"]},{'_id': False})
        username=user_info['username']
        # 선택한지역 넘겨주기
        if request.method == 'POST':
            want = request.form.get('inputGroupSelect04')
            # print(want)
            places = db.sample.find({"area": want}, {'_id': False})

            places = list(places)
            return render_template('2page-swiper''.html', data=want, places=places,token=token,username=username)
    except (jwt.exceptions.DecodeError,jwt.ExpiredSignatureError):
        flash('로그인을 해주세요!')
        return render_template("login.html")

    except:
        flash('로그인을 해주세요!')
        return render_template("login.html")


#명소의 자세한 페이지
@application.route('/detail',methods=['POST','GET'])
def show_detail():
    name = request.form['name_give']
    print(name)
    places = db.sample.find({"name": name}, {'_id': False})

    places = list(places)
    print(places)
    return {'result': places}


@application.route('/3page',methods=['GET'])
def show_detail2():
     token_receive=request.cookies.get('mytoken')
     print('3페이지에서받은토큰',token_receive)
     try:
         payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
         name = request.args.get('name')
         print(name)
         #명소에 대한 정보 불러오기
         places = db.sample.find({"name": name}, {'_id': False})
         #명소에 대한 리뷰 불러오기
         token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

         user_info = db.users.find_one({"username": payload["id"]},{'_id': False})
         username = user_info['username']
         reviews = list(db.reviews.find({"where": name}, {'_id': False}).sort([("reg_date", -1)]))
         places=list(places)
         reviews=list(reviews)
         if len(reviews)>3:
             reviews=reviews[0:3]

         #명소의 하트수세기
         heart_count=db.heart.count_documents({"place_name": name, "type": "heart"})
         #내가 하트 했는지
         heart_user=bool(db.heart.find_one({"place_name": name, "type": "heart", "username": payload['id']}))


         return render_template('3page-.html',place=places,reviews=reviews,place_heart=heart_count,heart_user=heart_user,token=token,username=username)

     except :
         flash('로그인을 해주세요!')
         return render_template("login.html")


#공공데이터 api query url 만드는함수
def get_request_query(url, operation, params, serviceKey):
    import urllib.parse as urlparse
    params = urlparse.urlencode(params)
    request_query = url + '/' + operation + '?' + params + '&' + 'serviceKey' + '=' + serviceKey
    return request_query

@application.route('/time',methods=['GET'])
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


@application.route('/reviewpage', methods=['GET'])
def go_reviews():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        place = request.args.get('place')
        user_info = db.users.find_one({"username": payload["id"]})
        username = user_info['username']
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        want_reviews = list(db.reviews.find({'where':place}, {'_id': False}))
        return render_template('review.html', reviews=want_reviews,place=place,token=token,username=username)
    except:
        flash('로그인을 해주세요!')
        return render_template("login.html")


@application.route('/myreviewpage', methods=['GET'])
def my_reviews():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.users.find_one({"username": payload["id"]})
        username=user_info['username']
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        want_reviews = list(db.reviews.find({}, {'_id': False}))
        return render_template('myreview.html', reviews=want_reviews,token=token,username=username)
    except:
        flash('로그인을 해주세요!')
        return render_template("login.html")


## API 역할을 하는 부분
@application.route('/reviewpage', methods=['POST'])
def write_review():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.users.find_one({"username": payload["id"]})
        # 어떤 명소인지
        username=user_info['username']
        title_receive=request.form['title_give']
        where_receive = request.form['where_give']

        review_receive = request.form['review_give']


        doc = {
            'writer':username,
            'where':where_receive,
            'title':title_receive,

            'review':review_receive,
            'reg_date': datetime.now(),
        }
        db.reviews.insert_one(doc)

        return jsonify({'msg': '저장완료!'})
    except:
        flash('로그인을 해주세요!')
        return render_template("login.html")


@application.route('/heart',methods=['POST'])
def update_heart():
    token_receive = request.cookies.get('mytoken')
    print(token_receive)
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.users.find_one({"username": payload["id"]})
        #어떤 명소인지
        place_receive = request.form["place_give"]
        type_receive = request.form["type_give"]
        #즐겨찾기 취소인지 실행인지
        place = db.sample.find_one({"name": place_receive})
        heart=place['heart_count']+1
        db.sample.update_one({"name": place_receive}, {'$set': {'heart_count':heart}})
        action_receive = request.form["action_give"]
        print("하트누른곳:",place_receive)
        print("하트누른곳:",type_receive,user_info['username'])
        doc = {
            "place_name": place_receive,
            "username": user_info["username"],
            "type": type_receive,

        }
        if action_receive == "like":
            db.heart.insert_one(doc)
        else:
            db.heart.delete_one(doc)

        count = db.heart.count({"place_name": place_receive})
        print(count)
        return jsonify({"result": "success", 'msg': 'updated', "count": count})


    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return redirect(url_for("index"))

if __name__ == '__main__':
    application.debug = True
    application.run()