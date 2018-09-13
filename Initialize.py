import string
from Socket import sendMessage
from Read import getOwner

# join the chat room of the intended user
def joinRoom(s):
    readbuffer = ""
    Loading = True
    while Loading:
        readbuffer = readbuffer + s.recv(1024)
        temp = string.split(readbuffer, "\n")
        readbuffer = temp.pop()
        
        for line in temp:
            print(line)
            Loading = loadingComplete(line)
    sendMessage(s, "Loading!")

	# checks if done connecting/loading chat
def loadingComplete(line):
	# we are done if we receieve the string "End of /NAMES list"
    if("End of /NAMES list" in line):
        return False
	# otherwise return true to indicate still loading
    else:
        return True
