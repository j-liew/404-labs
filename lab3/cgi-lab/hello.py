#!/usr/bin/env python3
import cgi
import cgitb
import templates

import os

print("Content-Type: text/html\n")
print()

#Q1
#print(os.environ)
# should see a bunch of unformatted text containing all environment variables going into server

# query string is empty

#Q2
#print(os.environ["HTTP_COOKIE"])

#Q2
#print(os.environ["QUERY_STRING"])


#Q3
#print(os.environ["HTTP_USER_AGENT"])
# Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0 

#Q4
# posts to itself, doesn't actually send it anywhere

print(templates.login_page())
s = cgi.FieldStorage()
username = s.getfirst("username")
password = s.getfirst("password")

print(username)
print(password)