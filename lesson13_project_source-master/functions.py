import json

def _load_posts_from_json():

    with open("posts.json", "r", encoding="utf-8") as fp:
        posts = json.load(fp)
    if posts:
        return posts
    return []


def get_posts_by_tag(tag_name):

    posts = _load_posts_from_json()
    posts_matching =[]
    search_for = f"#{tag_name}"

    for post in posts:
        if search_for in post.get("content"):
            posts_matching.append(post)

    return posts_matching


def _get_all_tags_from_str(string):

    tags = set()
    for word in string.split(" "):
        if word.startswith("#"):
            tags.add(word[1:])
    return tags


def get_all_tags_from_posts():

    posts = _load_posts_from_json()
    tags = set()
    for post in posts:
        post_content = post.get("content")
        tags_in_posts = _get_all_tags_from_str(post_content)
        tags = tags.union(tags_in_posts)

    return list(tags)

