from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

POSTS = [
    {"id": 1, "title": "First post", "content": "This is the first post."},
    {"id": 2, "title": "Second post", "content": "This is the second post."},
]


@app.route('/api/posts', methods=['GET'])
def get_posts():
    return jsonify(POSTS), 200


@app.route('/api/posts', methods=['POST'])
def add_posts():
    new_post = request.get_json()

    if "title" not in new_post and "content" not in new_post:
        return jsonify({"error": "Invalid post data (title and content missing)"}), 400
    if "title" not in new_post:
        return jsonify({"error": "Invalid post data (title missing)"}), 400
    if "content" not in new_post:
        return jsonify({"error": "Invalid post data (content missing)"}), 400
    
    new_id = max(post['id'] for post in POSTS) + 1
    new_post['id'] = new_id

    POSTS.append(new_post)

    return jsonify(new_post), 201


@app.route('/api/posts/<int:id>', methods=['DELETE'])
def delete_posts(id):
    post_with_id = [post for post in POSTS if post['id'] == id]

    if post_with_id == []:
        return jsonify({"error": f"Post id {id} not found"}), 404

    POSTS.remove(post_with_id[0])

    return jsonify({"message": f"Post with id {id} has been deleted successfully."}), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
