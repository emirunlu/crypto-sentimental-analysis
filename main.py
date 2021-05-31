import datetime
from analyzer.vader_analyzer import *
from crawler.get_reddit import *
from price_tracker.get_price import *

query               = "btc | bitcoin"    # Add your query
duration            = "7d"               # Select the timeframe. Epoch value or Integer + "s,m,h,d" (i.e. "second", "minute", "hour", "day")
size                = 1000               # maximum 1000 comments
sort_type           = "score"            # Sort by score (Accepted: "score", "num_comments", "created_utc")
sort                = "desc"             # sort descending
subs                = ["CryptoMarkets"]


comments_21d = search_subs_reddit(q=query,
                   before="22d",
                   after="28d",
                   size=size,
                   sort_type=sort_type,
                   sort=sort,
                   subreddit=subs)

comments_14d = search_subs_reddit(q=query,
                   before="15d",
                   after="21d",
                   size=size,
                   sort_type=sort_type,
                   sort=sort,
                   subreddit=subs)

comments_7d = search_subs_reddit(q=query,
                   before="8d",
                   after="14d",
                   size=size,
                   sort_type=sort_type,
                   sort=sort,
                   subreddit=subs)

date_21d = datetime.date.today() - datetime.timedelta(days=21)
date_14d = datetime.date.today() - datetime.timedelta(days=14)
date_7d = datetime.date.today() - datetime.timedelta(days=7)

scores_21d = analyze_sentences(comments_21d)
scores_14d = analyze_sentences(comments_14d)
scores_7d = analyze_sentences(comments_7d)

print("VADER score for days 22-28: ", scores_21d)
print("VADER score for days 15-21: ", scores_14d)
print("VADER score for days 14-8: ", scores_7d)

btc_price_21d = get_coingecko_price_history(date_21d.strftime("%d-%m-%Y"))
btc_price_14d = get_coingecko_price_history(date_14d.strftime("%d-%m-%Y"))
btc_price_7d = get_coingecko_price_history(date_7d.strftime("%d-%m-%Y"))

btc_price_22d = get_coingecko_price_history((date_21d - datetime.timedelta(days=1)).strftime("%d-%m-%Y"))
btc_price_15d = get_coingecko_price_history((date_14d - datetime.timedelta(days=1)).strftime("%d-%m-%Y"))
btc_price_8d = get_coingecko_price_history((date_7d - datetime.timedelta(days=1)).strftime("%d-%m-%Y"))

diff1 = btc_price_22d - btc_price_21d
diff2 = btc_price_15d - btc_price_14d
diff3 = btc_price_8d - btc_price_7d

average_diff_ratio = ((diff1 / scores_21d) + (diff2 / scores_14d) + (diff3 / scores_7d)) / 3
print("Average three week price/score ratio: ", average_diff_ratio)

comments = search_subs_reddit(q=query,
                   after=duration,
                   size=size,
                   sort_type=sort_type,
                   sort=sort,
                   subreddit=subs)

scores = analyze_sentences(comments)
print("VADER score for current week: ", scores)

current_btc_price = get_coingecko_price()
estimate_btc_price_24h = current_btc_price + (scores * average_diff_ratio)

print("Current bitcoin price: ", current_btc_price)
print("Estimated bitcoin price in 24h: ", estimate_btc_price_24h)