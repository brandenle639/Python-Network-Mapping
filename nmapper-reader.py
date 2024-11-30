#!/usr/bin/python3
import nmap, os

#The Input file
inpfile="Live-IP-List.txt"

#The output file
outputfile="nmapper.txt"

#initialize the port scanner
nmScan = nmap.PortScanner()

#Reads the input file
freader= open(inpfile,"r")

#Starts the file reading loop
while True:
    #Clears the terminal
    os.system('clear')
    # Get next line from file 
    line = freader.readline() 

    #Output the IP Address
    print(line)
    #Scans the IP Address
    nmScan.scan(line)

    #Exit if end of file is reached 
    if not line: 
     break
    #Opens file for writing
    routput=open(outputfile, "a")

    # run a loop to print all the found result about the ports
    for host in nmScan.all_hosts():
     routput.write("Host:" + host +"\n")
     routput.write("Host State: " + nmScan[host].state() +"\n")
     for proto in nmScan[host].all_protocols():
      routput.write('----------' +"\n")
      routput.write('Host Protocol(s): ' + proto +"\n")
      lport = nmScan[host][proto].keys()
      for port in lport:
       routput.write('port: '+ str(port) + "\tstate: " + str(nmScan[host][proto][port]['state'])+"\n")
    routput.write("##############################\n")
    routput.close()
