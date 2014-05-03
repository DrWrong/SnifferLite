#! /usr/bin/env python
# coding:utf-8

import os


class PromiscModel(object):

    """docstring for PromiscModel"""

    def __init__(self, ifname):
        super(PromiscModel, self).__init__()
        self.ifname = ifname

    def set_promisc_mode(self):
#		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#		a=fcntl.ioctl(s,
# 0x8913,#SIOCGIFFLAGS
#                  	struct.pack('24s', self.ifname))
#		print a
        try:
            os.setuid(0)
        except OSError as e:
            #raise OSError('请为程序设置suid 权限')
            print e
        if not self.test_promisc_mode():
            os.popen('ifconfig %s promisc' % self.ifname)

        return self.test_promisc_mode()

    def unset_promisc_mode(self):
        try:
            os.setuid(0)
        except OSError:
            raise OSError('请为程序设置suid权限')

        if self.test_promisc_mode():
            os.popen('ifconfig %s -promisc' % self.ifname)
        return not self.test_promisc_mode()

    def test_promisc_mode(self):

        result = os.popen('ifconfig %s' % self.ifname)
        res = False
        for eachline in result:
            if 'PROMISC' in eachline:
                res = True
        return res

if __name__ == '__main__':
    eth = PromiscModel('eth0')
    eth.set_promisc_mode()
