from flask import Flask, request, render_template, redirect,jsonify
from Classes.WordSearch import WordSearcher, BASE_URL
# from models import db, connect_db, User, Post, Tag, PostTag
# from sqlalchemy import desc
# from notes_search import BASE_URL
app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_ECHO'] = True

# connect_db(app)

# # creates tables in db if non exist.
# db.create_all()


##################################################


@app.route('/')
def landing():
    """Render Landing page"""

    return render_template("landing.html")

@app.route('/orlandoSearch')
def list_lecture_links():
    """Retrun all lecture links with word"""

    search_word = request.args.get('search-word', None)

    wc = WordSearcher(BASE_URL)
    links = wc.get_links(search_word)

    return jsonify(lecture_links=links)

