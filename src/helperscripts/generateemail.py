#!/usr/bin/python3

import uuid, json
from datetime import datetime
import glob 

print(f'Email Generator')

write_email = input ('Compose Email? ')
if write_email.lower() in ['y','yes']:
    mailmessage = {
        'id': str(uuid.uuid4()),
        'fromfield': input('Who is the email from (email address)? '),
        'fromfieldFriendly': input('Friendly name for the from email? '),
        'shortdate': datetime.utcnow().strftime('%a %b %d'),
        'longdate': datetime.utcnow().strftime("%A %B %d, %Y %I:%M %p"),
        'date': datetime.utcnow(),
        'categories': input('Categories (email, speaker, sponsor)? '),
        'subject': input('Subject? '),
        'message': input('Base64 encoded message? '),
        'attachment': input('Attachment File Name? ')
    }

    print(mailmessage)
    writemessagedialog = input('Write Message? ')

    if writemessagedialog.lower() in ["yes",'y']:
        with open(f'./data/{mailmessage["categories"]}/{mailmessage["id"]}.json','w') as output:
            output.write(json.dumps(mailmessage, default=str))
            output.close()

rebuildmailbox = input('Rebuild the mailbox? ')

mailboxfile = {
    'mailbox': []
}


if rebuildmailbox.lower() in ['yes','y']:
    # run through the emails
    emailFiles = glob.glob('./data/email/*.json', recursive=True)
    for file in emailFiles:
        with open(file,'r') as inputfile:
            data = inputfile.readline()
            mailboxfile['mailbox'].append(json.loads(data))

    mailboxfile['mailbox'].sort(key=lambda x: x['date'], reverse=True)
    with open(f'themes/bsb2021/static/data/mail.json', 'w') as mlbxfile:
        mlbxfile.write(json.dumps(mailboxfile,default=str))
    
    # run through the sponsors
    mailboxfile['mailbox'] = []
    sponsorFiles = glob.glob('./data/sponsor/*.json', recursive=True)
    for file in sponsorFiles:
        with open(file,'r') as inputfile:
            data = inputfile.readline()
            mailboxfile['mailbox'].append(json.loads(data))

    mailboxfile['mailbox'].sort(key=lambda x: x['date'], reverse=True)
    with open(f'themes/bsb2021/static/data/sponsor.json', 'w') as mlbxfile:
        mlbxfile.write(json.dumps(mailboxfile,default=str))

    # run through the speakers
    mailboxfile['mailbox'] = []
    speakerFiles = glob.glob('./data/speaker/*.json', recursive=True)
    for file in speakerFiles:
        with open(file, 'r') as inputfile:
            data = inputfile.readline()
            mailboxfile['mailbox'].append(json.loads(data))

    mailboxfile['mailbox'].sort(key=lambda x: x['date'], reverse=True)
    with open(f'themes/bsb2021/static/data/speaker.json', 'w') as mlbxfile:
        mlbxfile.write(json.dumps(mailboxfile,default=str))

    
