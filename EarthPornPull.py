import praw
import urllib

r = praw.Reddit(user_agent='EarthPornPull')
topTen = r.get_subreddit('EarthPorn').get_hot(limit=10)
urlList = []
for x in topTen:
    urlList.append(x.url)
count = 0
for x in urlList:
    count += 1
    if x.endswith('.jpg'):
        urllib.urlretrieve(x, str(count) + ".jpg")
    else:
        urllib.urlretrieve(x+".jpg", str(count) + ".jpg")

print "Done"