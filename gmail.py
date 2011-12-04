import email, getpass, imaplib, os

detach_dir = '.' # directory where to save attachments (default: current)
user = raw_input("Enter your GMail username: ")
pwd = getpass.getpass("Enter your password: ")
#mtuehuupknucnjyi

# connecting to the gmail imap server
m = imaplib.IMAP4_SSL("imap.gmail.com")
m.login(user,pwd)
m.select("INBOX") # here you a can choose a mail box like INBOX instead
# use m.list() to get all the mailboxes

print m.list()
resp, items = m.search(None, "ALL") # you could filter using the IMAP rules here (check http://www.example-code.com/csharp/imap-search-critera.asp)
items = items[0].split() # getting the mails id

recent1 =  m.recent()
print recent1[0].split()
for email in recent1[0].split():
    resp1, data1 = m.fetch(email, "(RFC822)")
    email_body1 = data1[0][1]
    mail1 = email.message_from_string(email_body1)
    print "["+mail1["From"]+"] :" + mail1["Subject"]
    
    
    
"""
counter = 0
print items
for emailid in items:
    counter = counter + 1
    
    if (counter > 10):
        break;
    resp, data = m.fetch(emailid, "(RFC822)") # fetching the mail, "`(RFC822)`" means "get the whole stuff", but you can ask for headers only, etc
    email_body = data[0][1] # getting the mail content
    mail = email.message_from_string(email_body) # parsing the mail content to get a mail object

    print "["+mail["From"]+"] :" + mail["Subject"]

    #Check if any attachments at all
    if mail.get_content_maintype() != 'multipart':
        continue


    # we use walk to create a generator so we can iterate on the parts and forget about the recursive headach
    for part in mail.walk():
        # multipart are just containers, so we skip them
        if part.get_content_maintype() == 'multipart':
            continue

        # is this part an attachment ?
        if part.get('Content-Disposition') is None:
            continue

        filename = part.get_filename()
        counter = 1

        # if there is no filename, we create one with a counter to avoid duplicates
        if not filename:
            filename = 'part-%03d%s' % (counter, 'bin')
            counter += 1

        att_path = os.path.join(detach_dir, filename)

        #Check if its already there
        if not os.path.isfile(att_path) :
            # finally write the stuff
            fp = open(att_path, 'wb')
            fp.write(part.get_payload(decode=True))
            fp.close()"""