import re
from Socket import sendMessage

# add message to list of blacklisted messages
def blacklistAdd(message):
    wordMessy = re.findall(r"\(+.*\)", message)
    word = str(wordMessy).strip("[").strip("]").strip("'").strip("(").strip(")")
    blackList = open("blacklist.json", "a")
    blackList.write("{0}\n".format(word))
    blackList.close()

