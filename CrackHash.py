from hash import hashing
from readw import  readall
import  signal




print """
        ##################################################
        ##                                              ##
        ##                                              ##
        ##                                              ##
        ##   Author @intx0x80                           ##
        ##                                              ##
        ##      Hash Cracking                           ##
        ##                                              ##
        ##################################################
"""

def signal_handler(signal, frame):

    print "\n[-] Exiting"

    exit()

signal.signal(signal.SIGINT, signal_handler)


Hashtxt=str(raw_input("Enter Hash TxT > "))
Typeh=str(raw_input("Ente Hash Type > "))
wordlist=str(raw_input("Enter File Path > "))


ha=hashing()
RD=readall()

rfile=RD.readfile(wordlist)
for i in rfile:
    i=i.strip("\n")

    hashtxt=ha.enc(str(i),Typeh)
    print " {0}::{1}".format(i,hashtxt)

    if Hashtxt.lower()==hashtxt:
        print "[+]  Hash Cracking  {0} :: {1} ".format(Hashtxt,i)
        break


__author__ = 'PikaChu'
