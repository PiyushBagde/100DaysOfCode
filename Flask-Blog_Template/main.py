import requests
from flask import Flask, render_template

from post import Post

app = Flask(__name__)

response = requests.get('https://api.npoint.io/c790b4d5cab58020d391').json()

post_obj = []
for post in response:
    instance = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_obj.append(instance)


@app.route('/')
def home():
    return render_template("index.html", blogs=post_obj)


@app.route('/post/<int:blog_id>')
def get_post(blog_id):
    requested_post = None
    for blog in post_obj:
        if blog.id == blog_id:
            requested_post = blog
    return render_template('post.html', blog=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
