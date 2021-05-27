import json
import requests

BASE_API_URL        = "https://api.pushshift.io"
SUBMISSION_API_URL  = "/reddit/search/submission/"
COMMENT_API_URL     = "/reddit/search/comment/"

query               = "test"        # Add your query
duration            = "30d"         # Select the timeframe. Epoch value or Integer + "s,m,h,d" (i.e. "second", "minute", "hour", "day")
size                = 1000          # maximum 1000 comments
sort_type           = "score"       # Sort by score (Accepted: "score", "num_comments", "created_utc")
sort                = "desc"        # sort descending
aggs                = "subreddit"   # "author", "link_id", "created_utc", "subreddit"

def search_subs_reddit(**kwargs):
    request = requests.get(BASE_API_URL + SUBMISSION_API_URL, params = kwargs)
    json_response = request.json()
    return json_response

print(search_subs_reddit(q=query,                 
                   after=duration,          
                   size=size,               
                   sort_type=sort_type,
                   sort=sort))