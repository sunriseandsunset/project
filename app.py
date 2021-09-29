from flask import Flask, render_template, jsonify, request,redirect,url_for
from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client.dbproject

@app.route('/')
def index():
    return render_template('douseesun.html')

'''

@app.route('/place',methods=['POST'])
def get_place():
    area_receive=request.form['place_give']
    
    return jsonify({'result':'sucess','msg':'지역 선택!'})
'''

#지역별 명소 데이터 api 가져오기
@app.route('/place',methods=['GET','POST'])
def show_place():
    #선택한지역 넘겨주기
    if request.method == 'POST':
        want = request.form.get('inputGroupSelect04')
        print(want)
        return render_template('douseesun2.html',data=want)
    '''   
    else:
        area = request.args.get('give_area')
        print(area)
        places = db.sample.find({"address": area}, {'_id': False})
        places=list(places)
        print(jsonify(places))
        #return jsonify(places)

        return render_template('douseesun2.html', data=area)

'''
'''
@app.route('/success')
def secondpage():
    #선택한지역 넘겨주기
    #area = request.args.get('give_area')
    return render_template('douseesun2.html', data=area)

'''




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000,debug=True)