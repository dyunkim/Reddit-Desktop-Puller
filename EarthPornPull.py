import praw
import urllib
import os

r = praw.Reddit(user_agent='EarthPornPull')
topTen = r.get_subreddit('EarthPorn').get_hot(limit=10)
urlList = []
for x in topTen:
    urlList.append(x.url)
count = 0
if os.path.isdir("Wallpapers") == False:
    os.makedirs("Wallpapers")
for x in urlList:
    count += 1
    imgName = str(count) + ".jpg"
    if x.endswith('.jpg'):
        urllib.urlretrieve(x, imgName)
    else:
        urllib.urlretrieve(x+".jpg", imgName)
    os.rename(imgName, "Wallpapers/" + imgName)

print "Done"