import requests


@app.route("/get_post")
def get_account():
    # Get the title from the request's parameters
    title = request.args.get("title")

    if not title:
        return "Title is required", 400

    # Make an API call to retrieve the post based on its title
    url = f"https://example.com/api/posts/{title}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()["content"]
    else:
        return "Failed to retrieve post", 500
