import praw
from pprint import pprint

APP_ID = "ctH2DqNEoJlxxE7DDpNYIQ"
APP_SECRET = "-"
    
base_url = 'https://www.reddit.com/'
data = {'grant_type': 'password','username': "teddy5760", "password": "-"}

reddit = praw.Reddit(
    client_id=APP_ID,
    client_secret=APP_SECRET,
    password="metodi2003",
    user_agent="SubMonitor by u/teddy5760",
    username="teddy5760"
)

subreddit = input("Choose a subreddit to display: ")

i = 1
for submission in reddit.subreddit(subreddit).new(limit=5):
    print(str(i) + ".", submission.title)
    i += 1