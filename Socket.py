import socket
import fileinput
from time import sleep
from Logger import log
from Settings import HOST, PORT, PASS, IDENT, CHANNEL
from datetime import datetime
from Read import getChannel

def openSocket():
    try:
        s = socket.socket()
        s.connect((HOST, PORT))
        s.send("PASS " + PASS + "\r\n")
        s.send("NICK " + IDENT + "\r\n")
        chanjoins = 'joins.txt'
        joinsfile = open(chanjoins, 'a+')
        joins = joinsfile.readlines()


        for sueless in joins:
                s.send("JOIN #" + str(sueless.strip()) + "\r\n")
                print "joined " + sueless.strip()
                sleep(0.2)
        
        joinsfile.close()
        
        return s
    except:
        print "Opensocket error"
        
def sendMessage(s, message):
    try:
        sleep(0.1)
        messageTemp = "PRIVMSG #" + str(CHANNEL) + " :" + str(message)
        s.send(messageTemp + "\r\n")
        time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        toLog = "Forcebotti: " + message.decode('utf8')
        log(toLog, CHANNEL)
    except:
        print "sendmessage error"

def sendChanMsg(s, chan, message):
    try:
        messageTemp = ("PRIVMSG #" + str(chan.strip()) + " :" + message)
        s.send(messageTemp.strip() + "\r\n")
        sleep(0.5)
        time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        toLog = "Forcebotti: " + message.decode('utf8')
        log(toLog, chan)
    except:
        print "sendmessage error"

def joinChan(s, chan):
    try:
        exists = 0
        addc = 0
        chanjoins = 'joins.txt'
        joinsfile = open(chanjoins, 'a+')
        joins = joinsfile.readlines()
        
        for somethings in joins:
                if joins[addc].strip().decode('utf8') == chan.decode('utf8'):
                        exists = 1
                addc = addc + 1

        if exists != 1:
                joinsfile.write(chan.encode('utf8') + '\n'.encode('utf8'))
                        
        joinsfile.close()
        
        s.send("JOIN #" + str(chan) + "\r\n")
    except:
        print "joinchan error"

def quitChan(s, chan):
    try:
        s.send("PART #" + str(chan) + "\r\n")

        chanjoins = 'joins.txt'
        joinsfile = open(chanjoins, 'a+')
        joins = joinsfile.readlines()
        poistettava = chan.strip()
                                                                
        for linja in fileinput.input(chanjoins, inplace=True):
                if poistettava.strip() == linja.strip():
                        continue
                print linja,

        fileinput.close()


    except:
        print "quitchan error"