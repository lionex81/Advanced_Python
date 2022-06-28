import json
import http
from flask import Flask, jsonify, request, make_response, Response
from user_api import user_router
from book_api import book_router

app = Flask(__name__)
app.register_blueprint(user_router)
app.register_blueprint(book_router)


@app.route('/')
def index():
    return "Hello world!"


@app.errorhandler(404)
def page_not_found(error):
    return "This page not found"


if __name__ == '__main__':
    app.run(debug=True)