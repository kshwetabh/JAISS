import speech
import feedparser


def readFeeds():
    url = "http://news.google.com/news?pz=1&cf=all&ned=us&hl=en&output=rss"
    rootfeed = feedparser.parse(url)
    speech.say("Today's top headlines")
    
    titles = []
    for entry in rootfeed["entries"]:
        titles.append(entry.title)
        print (entry.title)
    return titles
    #speech.say("That's all of today's top headlines")