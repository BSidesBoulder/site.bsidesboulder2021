#!/usr/bin/env python3

import glob
import json
import uuid

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
    message = {
        'id': uuid.uuid4(),
        'fromfieldFriendly': 'Sponsorship Services',
        'fromfield': 'sponsorship@bsidesboulder.org',
        'shortdate': '',
        'longdate': '',
        'date': '',
        'subject': f"{spon['level']} level sponsor - {spon['name']}"

    }

    output['mailbox'].append()
