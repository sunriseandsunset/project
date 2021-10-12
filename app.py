import flask
from flask import Flask, render_template, jsonify, request,redirect,url_for
from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup
import json
import xmltodict
import sys

app = Flask(__name__)

client = MongoClient('mongodb://test:test@localhost', 27017)
# client = MongoClient("mongodb://localhost:27017/")
db = client.dbproject

@app.route('/')
def index():
    # kimp = flask.Response()
    # kimp.headers["Access-Control-Allow-Origin"] = "*"
    return render_template('1page.html')


#지역별 명소 데이터 api 가져오기
@app.route('/place',methods=['GET','POST'])
def show_place():

    #선택한지역 넘겨주기
    if request.method == 'POST':
        want = request.form.get('inputGroupSelect04')
        #print(want)
        places = db.sample.find({"area": want}, {'_id': False})

        places=list(places)
        print(places)

        return render_template('2page.html',data=want,places=places)

def show_detail():
    if request.method == 'POST':
        want = request.form.get('inputGroupSelect04')
        # print(want)
        places = db.sample.find({"area": want}, {'_id': False})

        places = list(places)
        print(places)

        return render_template('2page.html', data=want, places=places)

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

    print('request_query:', request_query)
    response = requests.get(url=request_query)
    return response.text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000,debug=True)