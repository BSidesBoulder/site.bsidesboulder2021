#!/usr/bin/env python3

import glob
import json
import uuid

from datetime import datetime

sponsors = glob.glob('data/sponsor/**/*', recursive=True)

current_sponsors = []


# Read all of the sponsors and find the ones that have sent the check
for sponsor in sponsors:
    with open(sponsor,'r') as data:
        data_obj = json.loads(data.read())
        if data_obj['completed'] == True:
            current_sponsors.append(data_obj)


output = { 
    'mailbox': []
}

# Build the sponsors feed
for spon in current_sponsors:
    print(spon['completed_date'])
    dt = datetime.fromisoformat(spon['completed_date'])
    message = {
        'id': spon['id'],
        'fromfieldFriendly': 'Sponsorship Services',
        'fromfield': 'sponsorship@bsidesboulder.org',
        'shortdate': dt.strftime("%a %b %d"),
        'longdate': dt.strftime("%A %B %d, %Y %-I:%M %p"),
        'date': dt.strftime("%Y-%m-%d %H:%M:%S.%f"),
        'subject': f"{spon['level']} level sponsor - {spon['name']}"

    }

    output['mailbox'].append(message)

print(output)
