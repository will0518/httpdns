# Filename: httpdns.py
# @author: will
# -*- coding:utf-8 -*-  


import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import random
import re

from tornado.options import define, options

define("port", default=8000, help="run on the given port", type=int)

def findip(ss):
        file = open('host.txt')
        lines = file.readlines()
        iplist1=[]
        for line in lines:
                m = re.match(ss,line)
#               n = re.match(ss,line)
                if m:
                        temp1 = line.split('=',)[1].split('\n')[0].split(",")
                        iplist1.append(temp1)
#                       print iplist1
                        return iplist1[0]



class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        domain = self.get_argument('domain', '')
        print(domain)
        #iplist1 = ["1.1.1.1","2.2.2.2","3.3.3.3","4.4.4.4","5.5.5.5"]
        #iplist2 = ["114.114.114.114","115.115.115.115"]
        iplist1 = findip("aa")
        iplist2 = findip("bb")
        ip1 = random.choice(iplist1)
        ip2 = random.choice(iplist2)
        #ip = random.sample(iplist, 1)
        if domain == 'aa':
                #print ip
                #self.write("1.1.1.1")
                self.write(ip1)
        elif domain == 'bb':
                #print ip
                #self.write("1.1.1.1")
                self.write(ip2)
        else:
                self.write("null")


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


# cat host.txt 
#aa=1.1.1.1,5.5.5.5
#bb=3.3.3.3,4.4.4.4
