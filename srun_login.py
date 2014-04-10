import pycurl
import StringIO
import urllib

b = StringIO.StringIO()
c = pycurl.Curl()
host_address = '10.0.0.55'

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

uid = login(host_address, '444306422', '79fd042593849d8a')
print uid
