#!/usr/bin/env python3
import cgi
import cgitb
import templates
import secret
from http.cookies import SimpleCookie

import os

print("Content-Type: text/html")


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

#print(templates.login_page())
s = cgi.FieldStorage()
#print(s)
username = s.getfirst("username")
password = s.getfirst("password")


#print(username)
#print(password)

#Q5
form_ok = username == secret.username and password == secret.password 

c = SimpleCookie(os.environ["HTTP_COOKIE"])
c_username = None
c_password = None
if c.get("username"):
    c_username = c.get("username").value
if c.get("password"):
    c_password = c.get("password").value

cookie_ok = c_username == secret.username and c_password == secret.password

if cookie_ok:
    username = c_username
    password = c_password

if form_ok:
    print("Set-Cookie: username= ", username)
    print("Set-Cookie: password= ", password)
print()

#Q6

if not username and not password:
    print(templates.login_page())
elif username == secret.username and password == secret.password:
    print(templates.secret_page(username,password))
else:
    print(templates.after_login_incorrect())

