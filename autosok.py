#encoding: utf-8
import os
for i in range(6,256):
    os.system("firefox 192.168.2.%s &" % i)

