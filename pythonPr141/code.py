from flask import Flask, jsonify, request
import csv

all_articles = []

with open('data.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]


liked_articles=[]
not_liked_articles=[]
#did_not_watch=[]


app=Flask(__name__)


@app.route("/get-article")
def get_movie():
    return jsonify({
        "data":all_articles[0],
        "status":"success"
    })


@app.route("/liked-article", methods=["POST"])
def liked_movie():
    article = all_articles[0]
    all_article = all_articles[1:]
    liked_articles.append(article)
    return jsonify({
        "status": "success"
    }), 201



@app.route("/not-liked-article", methods=["POST"])
def not_liked_movie():
    article = all_articles[0]
    all_movie = all_articles[1:]
    not_liked_articles.append(article)
    return jsonify({
        "status": "success"
    }), 201




if __name__ == "__main__":
  app.run()



