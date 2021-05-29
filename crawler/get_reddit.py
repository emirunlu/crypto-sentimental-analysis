import json
import requests
import sys

BASE_API_URL        = "https://api.pushshift.io"
SUBMISSION_API_URL  = "/reddit/search/submission/"
COMMENT_API_URL     = "/reddit/search/comment/"

def search_subs_reddit(**kwargs):
    request = requests.get(BASE_API_URL + COMMENT_API_URL, params = kwargs)
    json_response = request.json()
    objects = json_response['data']
    comments = []
    for obj in objects:
        comments.append(obj['body'])
    return comments