import imaplib

def getUnreadMailCount():
    obj = imaplib.IMAP4_SSL('imap.gmail.com', int('993'))
    obj.login('uid', 'pwd') 
    obj.select()
    unreadCount = len(obj.search(None, 'UnSeen')[1][0].split())
    print unreadCount
    
    return unreadCount

getUnreadMailCount()