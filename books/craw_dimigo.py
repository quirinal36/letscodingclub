import feedparser
import time
import smtplib
from email.mime.text import MIMEText

# website's RSS feed URL
feed_url = "https://rss.blog.naver.com/aboutdimigo.xml"

# email credentials
smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = "turboguy36@gmail.com"
sender_password = "gvvttwiswmyjzrcb"
recipient_email = "coding-edu@kakao.com"

# initialize feedparser
last_published = None
feed = feedparser.parse(feed_url)

while True:
    # check if there are any new posts
    if feed.entries[0].published != last_published:
        # send email notification
        #print(f"feed.feed.title: {feed.feed.title}")
        #print(f"feed.entries[0].title: {feed.entries[0].title}")
        #print(f"feed.entries[0].link: {feed.entries[0].link}")
        
        message = f"Subject: New post on {feed.feed.title}\n\n{feed.entries[0].title}\n{feed.entries[0].link}"
        u = MIMEText(message.encode("utf-8"), _charset="UTF-8")
        u['Subject'] = '디미고 블로그 새글알림'
        print(u)
        #MIMEText(message.encode("utf-8")._charset="UTF-8")
        
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, u.as_string())
        # update last published time
        last_published = feed.entries[0].published
    
    # wait for some time before checking again
    time.sleep(3600*24) # check every 24 hours
    feed = feedparser.parse(feed_url)
