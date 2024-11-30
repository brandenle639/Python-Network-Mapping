#NOTE: Must be run with Root privilages
#!/usr/bin/python3
import os, time, datetime
from icmplib import ping, multiping, traceroute, Host, Hop

#Ip Address Markers
n1=1
n2=1
n3=1
n4=0

#The output file
outputfile="Traceroute-IP-List.txt"

#Checks to see if valid:
def validip(ip):
    return ip.count('.') == 3 and all(0<=int(num)<256 for num in ip.rstrip().split('.'))

#Gets the time when script started
stime=datetime.datetime.now()

#Loop until ip adress is 255.0.0.0
while n1 < 255:
    #Skip the 10.0.0.0 network
    if n1 == 10:
        n1=11
    #Skip the 172.16.0.0 network
    if n1 == 172 and n2 == 16:
        n2=32
    #Skip the 192.168.0.0 network
    if n1 == 192 and n2 == 168:
        n2=169
    #Skip the 127.0.0.0 network
    if n1 == 127:
        n1 = 128
    #Creates the Host IP Address
    hostname=str(n1)+"."+str(n2)+"."+str(n3)+"."+str(n4)
    #Clears the terminal
    os.system('clear')
    #Prints Current Host IP Adress
    print(hostname)
    #Traceroutes the IP Address, Maximum # of trachoppers, and sets fast mode
    trachoppers = traceroute(hostname, max_hops=255, fast_mode=True)
    #Keeps track of the hops
    last_distance = 0
    #Line output variable
    lnout=""
    #Sets if first part of the sentence
    lnfirst=0
    for hop in trachoppers:
        if last_distance + 1 != hop.distance:
            lnout=lnout + " -> " + "Some routers are not responding"
   
        # See the Hop class for details
        if lnfirst == 0:
         lnout=hop.address
         lnfirst=1
        else:
         lnout=lnout + " -> " + hop.address

        #Checks to see if an IP Adress is legitimately formated
        if validip(hop.address) == True:
         #Writes the ip address to the text list
         f = open(outputfile, "a")
         f.write(str(hop.address)+"\n")
         f.close()

        last_distance = hop.distance
    #Writes the ip address to the text list
    f = open(hostname+".txt", "a")
    f.write(str(lnout))
    f.close()

    #Increases the last digit of the IP Adress
    n4 = n4 + 1
    #Exits if the first digit is 255
    if n1 == 255:
        exit()
        n2 = n2 + 1
    #Increases the first digit and resets the second digit of the IP Address
    if n2 == 255:
        n2=0
        n1 = n1 + 1
    #Increases the second digit and resets the third digit of the IP Address
    if n3 == 255:
        n3=0
        n2 = n2 + 1
    #Increases the third digit and resets the fourth digit of the IP Address
    if n4 == 255:
        n4=0
        n3 = n3 + 1

#Gets the end time
etime=datetime.datetime.now()
#Subtracts the start time with end time to get completed time
dtime=etime-stime
#Writes completed time at the end of the text file
f = open(outputfile, "a")
f.write(str("\nTime it took to traceroute: "+ dtime))
f.close()
