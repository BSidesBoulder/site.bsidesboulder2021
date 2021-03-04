#!/usr/bin/python3

import uuid, json
from datetime import datetime
import glob 

print(f'Email Generator')

mailmessage = {
    'id': str(uuid.uuid4()),
    'fromfield': input('Who is the email from (email address)? '),
    'fromfieldFriendly': input('Friendly name for the from email? '),
    'shortdate': datetime.utcnow().strftime('%a %b %d'),
    'longdate': datetime.utcnow().strftime("%A %B %d, %Y %I:%M %p"),
    'date': datetime.utcnow(),
    'categories': input('Categories? '),
    'subject': input('Subject? '),
    'message': input('Base64 encoded message? '),
    'attachment': input('Attachment File Name? ')
}

print(mailmessage)
writemessagedialog = input('Write Message? ')

if writemessagedialog.lower() in ["yes",'y']:
    with open(f'./data/email/{mailmessage["id"]}.json','w') as output:
        output.write(json.dumps(mailmessage, default=str))
        output.close()

rebuildmailbox = input('Rebuild the mailbox? ')

mailboxfile = {
    'mailbox': []
}


if rebuildmailbox.lower() in ['yes','y']:
    emailFiles = glob.glob('./data/email/*.json', recursive=True)
    for file in emailFiles:
        with open(file,'r') as inputfile:
            data = inputfile.readline()
            print(data)
            mailboxfile['mailbox'].append(json.loads(data))

    mailboxfile['mailbox'].sort(key=lambda x: x['date'], reverse=True)
    with open(f'themes/bsb2021/static/data/mail.json', 'w') as mlbxfile:
        mlbxfile.write(json.dumps(mailboxfile,default=str))
