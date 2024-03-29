#!/usr/bin/python
import time
import random

def buildURL():
    # build random URL
    url_list=['www.largitdata.com', 'www.taiwanmobile.com', 'www.google.com']
    return random.choice(url_list)

def buildPath():
    # build random Path
    path_list=['/index.html', '/contact.html', '/contact/submit.html', '/about.html','/products.html','/services.html','/support.html']
    return random.choice(path_list)

def buildHTTP():
    # build random HTTP code
    a=200
    b=599
    return random.randrange(a,b,1)

def getHTTP():
    # build random HTTP status
    HTTP_status = [ 100, 101, 102, 200, 201, 202, 203, 204, 205, 206, 207, 226, 300, 301, 302, 303, 304, 305, 307, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 422, 423, 424, 426, 500, 501, 502, 503, 504, 505, 507, 510 ]
    return random.choice(HTTP_status)

def buildIP():
    # build random IP
    b1 = random.randrange(0, 255, 1)
    b2 = random.randrange(0, 255, 1)
    b3 = random.randrange(0, 255, 1)
    b4 = random.randrange(0, 255, 1)
    return str(b1) + '.' + str(b2) + '.' + str(b3) + '.' + str(b4)

log_File = open('/tmp/log-generator.log', 'w')

count = 0

while True:
  if(count > 1000):
    count = 0;
    time.sleep(5); 
  else:
    Http = getHTTP()
    count = count + 1
    Http = str(Http)
    Url = buildURL()
    Path = buildPath()
    Ip = str(buildIP())

    line = "HTTP %s %s %s %s"%(Http,Url,Path,Ip)
    print line
    log_File.write(line)

log_File.close()
