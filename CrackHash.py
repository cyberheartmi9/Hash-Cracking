from hash import hashing
from readw import  readall
import  signal




print """


                                                                            
                                                                            
HHHHHHHHH     HHHHHHHHH                                 hhhhhhh             
H:::::::H     H:::::::H                                 h:::::h             
H:::::::H     H:::::::H                                 h:::::h             
HH::::::H     H::::::HH                                 h:::::h             
  H:::::H     H:::::H    aaaaaaaaaaaaa      ssssssssss   h::::h hhhhh       
  H:::::H     H:::::H    a::::::::::::a   ss::::::::::s  h::::hh:::::hhh    
  H::::::HHHHH::::::H    aaaaaaaaa:::::ass:::::::::::::s h::::::::::::::hh  
  H:::::::::::::::::H             a::::as::::::ssss:::::sh:::::::hhh::::::h 
  H:::::::::::::::::H      aaaaaaa:::::a s:::::s  ssssss h::::::h   h::::::h
  H::::::HHHHH::::::H    aa::::::::::::a   s::::::s      h:::::h     h:::::h
  H:::::H     H:::::H   a::::aaaa::::::a      s::::::s   h:::::h     h:::::h
  H:::::H     H:::::H  a::::a    a:::::assssss   s:::::s h:::::h     h:::::h
HH::::::H     H::::::HHa::::a    a:::::as:::::ssss::::::sh:::::h     h:::::h
H:::::::H     H:::::::Ha:::::aaaa::::::as::::::::::::::s h:::::h     h:::::h
H:::::::H     H:::::::H a::::::::::aa:::as:::::::::::ss  h:::::h     h:::::h
HHHHHHHHH     HHHHHHHHH  aaaaaaaaaa  aaaa sssssssssss    hhhhhhh     hhhhhhh
                                                                            
                                                                            
                                                                            
                                                                            
                                                                            
            
                      _             
                     | |            
   ___ _ __ __ _  ___| | _____ _ __ 
  / __| '__/ _` |/ __| |/ / _ \ '__|
 | (__| | | (_| | (__|   <  __/ |   
  \___|_|  \__,_|\___|_|\_\___|_|   
                                    
                                    
                                                                
                                                                            



Author @intx0x80                           
        
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
