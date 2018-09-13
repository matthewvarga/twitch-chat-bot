import string
import sys
import re
import random
from Read import getUser, getMessage, getOwner
from Socket import openSocket, sendMessage
from Initialize import joinRoom
from Commands import blacklistAdd
from time import *

# connect to the chat room
s = openSocket()
joinRoom(s)
readbuffer = ""

while True:
    readbuffer = readbuffer + s.recv(1024)
    # message sent to chat room, will be checked for commands then move to next
    temp = string.split(readbuffer, "\n")
    readbuffer = temp.pop()
    
    # check if any commands in each line of message
    for line in temp:
	# PING command
        if "PING :tmi.twitch.tv" in line:
            s.send(line.replace("PING", "PONG"))
            print "pong"
            break
        user = getUser(line)
        message = getMessage(line)
        userMessage = "{0}:{1}".format(user, message)
        print userMessage
		
	# KIll command issued by channel owner - disconnects bot from channel
        if "#kill" in message and user == getOwner():
            sendMessage(s, "/disconnect")
            sys.exit()
            break

	# BLACKLISTADD command issued, updated blacklist with the provided message
        elif "#blacklistAdd" in message and user == getOwner():
            blacklistAdd(message)
            sendMessage(s, "added to blacklist!")
            break

	# RANDOM command issued, outputs a random number from 0 to 10
        elif "#random" in message:
            randInt = random.randint(0,10)
            sendMessage(s, "random number: {0}".format(randInt))
            print randInt

	#SPAM command issued, spams a bunch of letters in the chat
        elif "#spam" in message:
            spam = ["a", "b" , "c" , "d" , "e" , "f" , "g" , "h" , "i" , "j" ]
            for i in range(0, len(spam)):
                sendMessage(s, spam[i])
                sleep(0.01)
            break
