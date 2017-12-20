from twitter import *
from .api_key import *

t = Twitter(auth=OAuth(
    token= Access_Token,
    token_secret= Access_Token_Secret,
    consumer_key=Consumer_Key,
    consumer_secret=Consumer_Secret
))

statusUpdate = t.statuses.update(status='Hello, world!')
print(statusUpdate)