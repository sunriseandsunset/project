from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client.dbStock


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/post', methods=['POST'])
def save_post():
    doc = {'idx': 'index', 'title': 'title', 'content': 'content', 'reg_date': 'date'}
    db.post.insert_one(doc)
    return {"result": "success"}


@app.route('/post', methods=['GET'])
def get_post():
    data = list(db.post.find({}, {'_id': False})
    return {"result": "success"}


@app.route('/post', methods=['DELETE'])
def delete_post():
    return {"result": "success"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)