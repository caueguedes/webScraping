from twitter import *
from .api_key import *

t = Twitter(auth=OAuth(
    token=Access_Token,
    token_secret=Access_Token_Secret,
    consumer_key=Consumer_Key,
    consumer_secret=Consumer_Secret
))

pythonStatuses = t.statuses.user_timeline(screen_name="montypython", count=5)
print(pythonStatuses)