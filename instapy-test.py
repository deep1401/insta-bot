from instapy import InstaPy
from selenium import webdriver
username=input("Enter username: ")
password=input("Enter password: ")
InstaPy(username=username,password=password).login()
