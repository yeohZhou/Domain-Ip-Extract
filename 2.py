#!/usr/bin/python
import re
import sys

'''def readText(txtpath):
    fp = open(txtpath,'r')
    ff = fp.read()
    fp.close()
    return ff
'''

def extractIp(data):
    ipPattern = re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
    findIP = re.findall(ipPattern,data)
    ip = list(set(findIP))
    ip = sorted(ip)
    for i in ip:
        print i

def readText(txtpath):
    fp = open(txtpath,'r')
    ff = []
    while 1:
        line = fp.readline().strip('\n')
        if not line:
            break
        ff.append(line)
    fp.close()
    return ff

def extractPort(txtpath):
    fp = open(txtpath,'r')
    ff = []
    while 1:
        line = fp.readline().strip('\n')
        ipPattern = re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
        findIP = re.findall(ipPattern,line)
        portPattern = re.compile('(\d+)/tcp')
        findPort = re.findall(portPattern,line)
        if len(findIP)!=0 and len(findPort)!=0:
            line = 'http://'+findIP[0]+':'+findPort[0]+'/'
            print line
        if not line:
            break
        ff.append(line)
    fp.close()


def extractDomain(data):
    domainPattern = re.compile(r'[a-zA-Z0-9]*\.{0,1}[a-zA-Z0-9]*\.{0,1}[a-zA-Z0-9]*\.{0,1}[a-zA-Z0-9]*\.{0,1}[a-zA-Z0-9]*\.{0,1}[a-zA-Z0-9]+\.{1}[a-zA-Z]+')
    findDomain = re.findall(domainPattern,data)
    domain = list(set(findDomain))
    domain = sorted(domain)
    for i in domain:
        print i

if __name__ == "__main__":
#try:
    data = readText(sys.argv[1])
    for opt in sys.argv:
        if opt == 'ip':
            extractIp(data)
            break
        if opt == 'domain':
            extractDomain(data)
            break
        if opt == 'port':
            extractPort(sys.argv[1])
#except:
    #print 'usage: ' + sys.argv[0] + ' FileName' +' {ip,domain,port}'
