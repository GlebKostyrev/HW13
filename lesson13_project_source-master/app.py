from flask import Flask, request, render_template, redirect, send_from_directory
from functions import get_posts_by_tag, get_all_tags_from_posts, dumps_post
import imghdr

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)


@app.route("/")
def page_index():

    tags = get_all_tags_from_posts()
    return render_template("index.html", tags=tags)


@app.route("/tag")
def page_tag():
    tag_name = request.args.get('tag')
    posts = get_posts_by_tag(tag_name)
    return render_template("post_by_tag.html", tag=tag_name, posts=posts)


@app.route("/post", methods=["GET"])
def page_post_form():
    return render_template("post_form.html")



@app.route("/post", methods=["POST"])
def page_post_create():

    picture = request.files.get("picture")
    content = request.values.get("content")

    if not picture or not content:
        return redirect("/post")

    image_type = imghdr.what(picture)
    if not image_type:
        return redirect("/post")

    filename = picture.filename
    path = "./"+UPLOAD_FOLDER+"/"+filename
    picture.save(path)

    picture_new_url = "/"+UPLOAD_FOLDER+"/"+filename

    new_posts = {"pic": path, "content": content}
    dumps_post(new_posts)

    return render_template("post_uploaded.html", picture=picture_new_url, content=content)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()

