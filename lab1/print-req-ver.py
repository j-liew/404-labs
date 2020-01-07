import requests
print (requests.__version__)

#google=requests.get("https://google.com/teapot")
#print(google)

res = requests.get ("https://raw.githubusercontent.com/j-liew/404-labs/master/lab1/print-req-ver.py")
print(res.content)