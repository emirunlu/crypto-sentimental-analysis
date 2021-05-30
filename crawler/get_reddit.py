import json
import requests
import sys
import datetime
unix_epoch = datetime.datetime(1970, 1, 1)


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

def utc_to_epoch(utc_date):
    date = datetime.datetime.strptime(utc_date, "%d-%m-%y")
    # date = utc_date
    epoch = (date - unix_epoch).total_seconds()
    return int(epoch)