from analyzer.vader_analyzer import *
from analyzer.data import *
from crawler.get_reddit import *
from price_tracker.get_price import *

query               = "btc | bitcoin"   # Add your query
duration            = "7d"             # Select the timeframe. Epoch value or Integer + "s,m,h,d" (i.e. "second", "minute", "hour", "day")
size                = 1000               # maximum 1000 comments
sort_type           = "score"           # Sort by score (Accepted: "score", "num_comments", "created_utc")
sort                = "desc"            # sort descending
subs                = ["wallstreetbets"]

comments = search_subs_reddit(q=query,
                   after=duration,
                   # after=utc_to_epoch(""),
                   # before=utc_to_epoch(""),
                   size=size,
                   sort_type=sort_type,
                   sort=sort,
                   subreddit=subs)

scores = analyze_sentences(comments)

current_btc_price = get_coingecko_price()