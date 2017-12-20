from twitter import Twitter, OAuth
from .api_key import *

t = Twitter(auth=OAuth(token=api_key.Access_Token,
                       token_secret=api_key.Access_Token_Secret,
                       consumer_key=api_key.Consumer_Key,
                       consumer_secret=api_key.Consumer_Secret))

pythonTweets = t.search.tweets(q = "#python")
print(pythonTweets)