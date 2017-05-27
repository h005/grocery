import urllib
import urllib2
import getpass

# read in the username
username = raw_input('username:')

# read in the password without display
password = getpass.getpass()


values = {}
values['username'] = username
values['password'] = password

data = urllib.urlencode(values)

url = "http://p.nju.edu.cn/portal_io/login"

request = urllib2.Request(url,data)
reponse = urllib2.urlopen(request)

context = reponse.read()

msg = context.split(',')

# print the login state
for ele in  msg:
    if ele.split(':')[0] == '"reply_msg"':
        print ele.split(':')[1]
        break
