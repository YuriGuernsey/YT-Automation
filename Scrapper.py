import praw
import requests
 
reddit_read_only = praw.Reddit(client_id="6K2ytW1Qy5Jf2c4UGBrFcg",client_secret="OAPD27pu49M2QWbRcgW33VTkEoXZQg", user_agent="scrapper by /u/chuckykillr")
 
 
subreddit = reddit_read_only.subreddit("ProgrammerHumor")
x = 1
for post in subreddit.hot(limit=100000):
  if '.gif' in post.url:
    r = requests.get(post.url, allow_redirects=True)
    open('clips/img-' + str(x) +'.gif', 'wb').write(r.content)
    x += 1