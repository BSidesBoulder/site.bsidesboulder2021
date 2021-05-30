#!/usr/bin/env python3

import glob
import json
import uuid

from datetime import datetime
import base64

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

    body = f"""

    <div class="sponsor-image">
        <img src="/img/sponsor/{spon['image']}" />
    </div>

    <div class="sponsor-note">
        We would like to welcome our sponsor {spon['name']} at the {spon['level']} level. {spon['note']}
    </div>
    <br />
    <br />

    <div class="sponsor-website">
        <strong>Website: </strong> <a href="{spon['web']}" target="_blank">{spon['web']}</a>
    </div>

    <div class="sponsor-twitter">
        <strong>Twitter: </strong> <a href="https://www.twitter.com/{spon['twitter'].replace('@','')}" target="_blank">{spon['twitter']}</a>
    </div>
    

    """

    message = {
        'id': spon['id'],
        'fromfieldFriendly': 'Sponsorship Services',
        'fromfield': 'sponsorship@bsidesboulder.org',
        'shortdate': dt.strftime("%a %b %d"),
        'longdate': dt.strftime("%A %B %d, %Y %-I:%M %p"),
        'date': dt.strftime("%Y-%m-%d %H:%M:%S.%f"),
        'subject': f"{spon['level']} level sponsor - {spon['name']}",
        'message': base64.encodebytes(body.encode()).decode()

    }

    output['mailbox'].append(message)

with open('themes/bsb2021/static/data/sponsor.json','w') as ofile:
    ofile.write(json.dumps(output))
    ofile.close()
