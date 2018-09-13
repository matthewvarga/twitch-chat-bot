import string
from Settings import CHANNEL

# retrieves a users name from the chat message
# line = single chat message, including name and message, formatted as 'name:message' (string)
def getUser(line):
    separate = line.split(":", 2)
    user = separate[1].split("!", 1)[0]
    return user
	
# retrieves the message portion of the chat message
# line = single chat message, including name and message, formatted as 'name:message' (string)
def getMessage(line):
    separate = line.split(":", 2)
    message = separate[2]
    return message
	
# retrieves the channel owner
def getOwner():
    owner = CHANNEL
    return owner
    
