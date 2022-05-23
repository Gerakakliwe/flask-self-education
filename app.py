from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def main_page():
    return '<p>Main page</p>'


@app.route('/user/<int:user_id>')
def show_user_profile(user_id):
    return f'User {escape(user_id)}'


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post {post_id}'
