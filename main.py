import feedparser


def rss(url):
    try:
        d = feedparser.parse(url)
        for x in d.entries:
            print(x.title)
            print(x.links)
            print(x.description)
            max_len = max(len(x.description), len(x.title))
            print("-" * max_len)
    except:
        print("Not a RSS Url")


a = input("Enter a RSS Url: ")
rss(a)
