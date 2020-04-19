from instapy import InstaPy
from selenium import webdriver
username=input("Enter username: ")
password=input("Enter password: ")
session=InstaPy(username=username,password=password)
#Preventing bot detection
session.set_quota_supervisor(enabled=True,peak_comments_daily=240, peak_comments_hourly=21)
#Logging into the session
session.login()
#Liking based on usernames
session.like_by_users(['instagram','design'],amount=5)
#Preventing spam likes
session.set_dont_like(["naked", "nsfw"])
#Follow all users whose images were liked
session.set_do_follow(True,percentage=100)
session.set_do_comment(True, percentage=67)
session.set_comments(['This is some amazing content',"Wow","Nice posts!"])
session.end()
session.set_quota_supervisor(enabled=True)

