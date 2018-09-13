import socket
from Settings import HOST, PORT, PASS, IDENT, CHANNEL

# open socket with the desired users twitch chat
def openSocket():	
    s = socket.socket()
    s.connect((HOST, PORT))
    s.send("PASS {0}\r\n".format(PASS))
    s.send("NICK " + IDENT + "\r\n")
    s.send("JOIN #" + CHANNEL + "\r\n")
    return s

# sends message to the chat channel
def sendMessage(s, message):
    messageTemp = "PRIVMSG #" + CHANNEL + " :" + message
    s.send(messageTemp + "\r\n")
    print("Sent: " + messageTemp)
