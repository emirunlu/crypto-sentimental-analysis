import json
import requests

BASE_API_URL = "https://api.pushshift.io"
SUBMISSION_API_URL = "/reddit/search/submission/"
COMMENT_API_URL = "/reddit/search/comment/"
LIMIT_SUBMISSIONS = 100

keywords = [""]

def search_subs_reddit(query):
    request = requests.get(BASE_API_URL + SUBMISSION_API_URL + f"?q={query}")
    json_response = request.json()
    return json_response

print(search_subs_reddit("test"))